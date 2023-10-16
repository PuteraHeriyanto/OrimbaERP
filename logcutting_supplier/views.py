from django.contrib.auth.decorators import login_required
from django.db.models import Q
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
from .forms import SupplierInputForm
from .models import Supplier
from .utils import set_pagination
from django.db import IntegrityError
from django.db.models import Max
from django.utils.safestring import mark_safe


# class SawnLogCreateView(SuccessMessageMixin, CreateView):                                
#     # model = SawnLog                                                                  
#     form_class = SawnLogInputForm                                                         
#     template_name = "app/sawnlog/input_data.html"                                                          
#     success_url = 'sawnlog/new'                                                                   
#     success_message = "Sawn Log has been created successfully"                            

    
#     def get_context_data(self, **kwargs):                                               
#         context = super().get_context_data(**kwargs)
#         context["title"] = 'Input Data Sawn Log'
#         context["savebtn"] = 'Add to Sawn Log'
#         return context   
    
class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierInputForm
    template_name = "app/supplier/input_data.html"
    success_url = reverse_lazy('supplier')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Input Data Supplier'
        context["savebtn"] = 'Add to Supplier'
        return context

    # def form_valid(self, form):
    #     log_id = form.cleaned_data['log_id']
    #     sawn_id = form.cleaned_data['sawn_id']

    #     for i in range(1, int(sawn_id) + 1):
    #         try:
    #             SawnLog.objects.create(log_id=log_id, sawn_id=f"{log_id}-{i}")
    #         except IntegrityError:
    #         # Handle the duplicate key violation here, e.g., by setting an error message
    #             error_message = "<span style='color:red;'>Log ID Already Exists</span>"
    #             form.add_error(None, mark_safe(error_message))
    #             return self.form_invalid(form)

    #     try:
    #         log_list_item = LogList.objects.get(log_id=log_id)
    #         log_list_item.stock = 0
    #         log_list_item.save()
    #     except LogList.DoesNotExist:
    #         pass

    #     # Loop through and delete records with only numeric sawn_id values
    #     for record in SawnLog.objects.filter(log_id=log_id):
    #         if record.sawn_id.isnumeric():
    #             record.delete()

    #     return super().form_valid(form)
    
   


# You can define your `update_stock` view separately if needed.

# def update_stock(request):
#     if request.method == 'POST':
#         form = SawnLogForm(request.POST)
#         if form.is_valid():
#             log_id = form.cleaned_data['log_id']
#             try:
#                 log_list_item = LogList.objects.get(log_id=log_id)
#                 log_list_item.stock = 0
#                 log_list_item.save()
#             except LogList.DoesNotExist:
#                 pass
#             SawnLog.objects.create(log_id=log_id)
#             return redirect('success_view')
#     else:
#         form = SawnLogForm()
#     return render(request, 'app/sawnlog/list.html', {'form': form})

            


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


class SupplierView(View):
    context = {'segment': 'supplier'}

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
        return redirect('supplier')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        supplier = self.get_object(pk)
        supplier.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deleted successfully')
            redirect_url = reverse('supplier')

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
                        filter_params = Q(supplier_id_for__icontains=key.strip())
                    else:
                        filter_params |= Q(supplier_id_for__icontains=key.strip())

        suppliers = Supplier.objects.filter(filter_params) if filter_params else Supplier.objects.all()

        self.context['suppliers'], self.context['info'] = set_pagination(request, suppliers)
        if not self.context['suppliers']:
            return False, self.context['info']

        return self.context, 'app/supplier/list.html'

    def edit(self, request, pk):
        supplier = self.get_object(pk)

        self.context['supplier'] = supplier
        self.context['form'] = SupplierInputForm(instance=supplier)

        return self.context, 'app/supplier/edit.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        supplier = self.get_object(pk)
        form = SupplierInputForm(instance=supplier)
        context = {'instance': supplier, 'form': form}
        return render_to_string('app/supplier/edit_row.html', context)

    """ Common methods """

    def get_object(self, pk):
        supplier = get_object_or_404(Supplier, supplier_id=pk)
        return supplier

    def get_row_item(self, pk):
        supplier = self.get_object(pk)
        edit_row = render_to_string('app/supplier/edit_row.html', {'instance': supplier})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        supplier = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = SupplierInputForm(form_data, instance=supplier)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Data saved successfully')

            return True, 'Data saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'
    
    
   
