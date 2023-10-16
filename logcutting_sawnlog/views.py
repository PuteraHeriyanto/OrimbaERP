from django.db import IntegrityError, connection
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F, IntegerField, Case, When, Value
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse, QueryDict
from django import template
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (View, CreateView, UpdateView)
from .forms import SawnLogInputForm, SawnLogForm, SawnLogEditForm
from .models import SawnLog, LogList, SawnLogInput
from .utils import set_pagination
from django.db.models import Max
from django.utils.safestring import mark_safe
from django.db.models.functions import Cast
from django.db.models import IntegerField
from django.http import JsonResponse



    
class SawnLogCreateView(CreateView):    
    model = SawnLogInput
    form_class = SawnLogInputForm
    template_name = "app/sawnlog/input_data.html"
    success_url = reverse_lazy('sawnlog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Input Data Sawn Log'
        context["savebtn"] = 'Add to Sawn Log'
        return context
    

    def form_valid(self, form):
        log_id = form.cleaned_data['log_id']
        sawn_id = form.cleaned_data['sawn_id']


        if sawn_id.isdigit() and int(sawn_id) > 0:
            for i in range(1, int(sawn_id) + 1):
                try:
                    SawnLogInput.objects.create(log_id=log_id, sawn_id=f"{log_id}-{i}")
      
                except IntegrityError:
                    # Handle the duplicate key violation here, e.g., by setting an error message
                    error_message = "<span style='color:red;'>Log ID Already Exists</span>"
                    form.add_error(None, mark_safe(error_message))
                    return self.form_invalid(form)  

        try:
            log_list_item = LogList.objects.get(log_id=log_id)
            log_list_item.stock = 0
            log_list_item.save()
        except LogList.DoesNotExist:
            pass

        return super().form_valid(form)
    
    def form_invalid(self, form):

        return super().form_invalid(form)
    


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


class SawnLogView(View):
    context = {'segment': 'sawnlogs'}

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
        return redirect('sawnlog')
    

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})



    # def delete(self, request, pk, action=None):
    #     # Get the specific SawnLog record to be deleted
    #     sawnlog = get_object_or_404(SawnLog, pk=pk)

    #     # Get the log_id value of the record to be deleted
    #     log_id_value = sawnlog.log_id

    #     # Find all records with the same log_id value
    #     related_logs = SawnLog.objects.filter(log_id=log_id_value)

    #     # Delete all related records
    #     related_logs.delete()

    #     # Optionally, you can delete the original record as well
    #     sawnlog.delete()

    #     # Update the stock in LogList
    #     try:
    #         log_list_item = LogList.objects.get(log_id=log_id_value)
    #         log_list_item.stock = 1  # Set the stock value to 1
    #         log_list_item.save()
    #     except LogList.DoesNotExist:
    #         log_list_item = LogList(log_id=log_id_value, stock=1)
    #         log_list_item.save()

    #     redirect_url = None
    #     if action == 'single':
    #         messages.success(request, 'Item(s) deleted successfully')
    #         redirect_url = reverse('sawnlogs')

    #     response_data = {
    #         'valid': 'success',
    #         'message': 'Item(s) deleted successfully',
    #         'redirect_url': redirect_url,
    #     }

    #     return JsonResponse(response_data)

    def delete(self, request, pk, action=None):
        sawnlog = self.get_object(pk)
        log_id_value = sawnlog.log_id

        # Delete the record from sawnlog
        sawnlog.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deleted successfully')
            redirect_url = reverse('sawnlogs')

        # Check if log_id_value exists in LogList
        log_ids_in_sawnlog = set(sawnlog.log_id for sawnlog in SawnLog.objects.all())

        # Iterate through LogList and update stock to 1 for log_ids not in sawnlog
        for log_list_item in LogList.objects.all():
            if log_list_item.log_id not in log_ids_in_sawnlog:
                log_list_item.stock = 1
                log_list_item.save()

        response_data = {
            'valid': 'success',
            'message': 'Item(s) deleted successfully',
            'redirect_url': redirect_url,
        }

        return JsonResponse(response_data)
    
       
        

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(sawn_id__icontains=key.strip())
                    else:
                        filter_params |= Q(sawn_id__icontains=key.strip())

        sawnlogs = SawnLog.objects.filter(filter_params) if filter_params else SawnLog.objects.all()

        self.context['sawnlogs'], self.context['info'] = set_pagination(request, sawnlogs)
        if not self.context['sawnlogs']:
            return False, self.context['info']

        return self.context, 'app/sawnlog/list.html'

    def edit(self, request, pk):
        sawnlog = self.get_object(pk)

        self.context['sawnlog'] = sawnlog
        self.context['form'] = SawnLogEditForm(instance=sawnlog)
        

        return self.context, 'app/sawnlog/edit.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        sawnlog = self.get_object(pk)
        form = SawnLogForm(instance=sawnlog)
        context = {'instance': sawnlog, 'form': form}
        return render_to_string('app/sawnlog/edit_row.html', context)

    """ Common methods """

    def get_object(self, pk):
        sawnlog = get_object_or_404(SawnLog, sawn_id=pk)
        return sawnlog
     

    def get_row_item(self, pk):
        sawnlog = self.get_object(pk)
        edit_row = render_to_string('app/sawnlog/edit_row.html', {'instance': sawnlog})
        return edit_row
    

    def update_instance(self, request, pk, is_urlencode=False):

        sawnlog = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = SawnLogEditForm(form_data, instance=sawnlog)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Data saved successfully')

            return True, 'Data saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'
    

    
    
   
