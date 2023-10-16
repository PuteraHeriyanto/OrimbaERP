from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse, QueryDict
from django import template
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (View, CreateView, UpdateView)
from .forms import LogListInputDataForm
from .forms import LogListForm
from .models import LogList
from .utils import set_pagination


class LogListDataCreateView(SuccessMessageMixin, CreateView):                                 # createview class to add new LogListData, mixin used to display message
    # model = LogListData                                                                       # setting 'LogListData' model as model
    form_class = LogListInputDataForm                                                         # setting 'LogListDataForm' form as form
    template_name = "app/loglist/input_data.html"                                                          # 'edit_data.html' used as the template
    success_url = 'loglistnew'                                                                  # redirects to 'LogList' page in the url after submitting the form
    success_message = "Log List has been created successfully"                             # displays message when form is submitted

    
    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Input Data Log List'
        context["savebtn"] = 'Add to Log List'
        return context   


# @login_required(login_url="/login/")
# def index(request):
#     context = {'segment': 'index'}
#     html_template = loader.get_template('index.html')
#     return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]
#         context['segment'] = load_template

#         html_template = loader.get_template(load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:

#         html_template = loader.get_template('page-500.html')
#         return HttpResponse(html_template.render(context, request))


class LogListView(View):
    context = {'segment': 'loglists'}

    def get(self, request, pk=None, action=None):
        if request.is_ajax():
            if pk and action == 'edit':
                edit_row = self.edit_row(pk)
                return JsonResponse({'edit_row': edit_row})
            elif pk and not action:
                edit_row = self.get_row_item(pk)
                return JsonResponse({'edit_row': edit_row})

        if pk and action == 'edit':
            context, template = self.edit(request, pk)
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('loglist')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        loglist = self.get_object(pk)
        loglist.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deleted successfully')
            redirect_url = reverse('loglists')

        response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(log_id_for__icontains=key.strip())
                    else:
                        filter_params |= Q(Log_id_for__icontains=key.strip())

        loglists = LogList.objects.filter(filter_params) if filter_params else LogList.objects.all()

        self.context['loglists'], self.context['info'] = set_pagination(request, loglists)
        if not self.context['loglists']:
            return False, self.context['info']

        return self.context, 'app/loglist/list.html'

    def edit(self, request, pk):
        loglist = self.get_object(pk)

        self.context['loglist'] = loglist
        self.context['form'] = LogListForm(instance=loglist)

        return self.context, 'app/loglist/edit.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        loglist = self.get_object(pk)
        form = LogListForm(instance=loglist)
        context = {'instance': loglist, 'form': form}
        return render_to_string('app/loglist/edit_row.html', context)

    """ Common methods """

    def get_object(self, pk):
        loglist = get_object_or_404(LogList, log_id=pk)
        return loglist

    def get_row_item(self, pk):
        loglist = self.get_object(pk)
        edit_row = render_to_string('app/loglist/edit_row.html', {'instance': loglist})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        loglist = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = LogListForm(form_data, instance=loglist)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Data saved successfully')

            return True, 'Data saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'
    
    
    # def update_instance(self, request, pk):
    #     loglists2 = self.get_object(pk)  # You need to define the get_object method correctly
    #     if request.method == 'POST':
    #         form = LogListForm(request.POST, instance=loglists2)
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, 'Data saved successfully')
    #             return HttpResponse(status=200)  # Return an appropriate response
    #     else:
    #             messages.warning(request, 'Error occurred. Please try again.')

    #     return HttpResponse(status=400) 

