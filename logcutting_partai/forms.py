from django import forms
# from .models import LogList
from django.db.models import F, Func
from .models import Partai
from .models import Supplier
# from .models import Species


class PartaiForm(forms.ModelForm):

    # log_id = forms.CharField(label="Log ID", widget=forms.TextInput(attrs={'class': 'form-control loglist'}))

    partai_id = forms.CharField(label="Partai ID", widget=forms.TextInput(attrs={'class': 'form-control partai'}))
    supplier_id = forms.CharField(label="Supplier ID", widget=forms.TextInput(attrs={'class': 'form-control partai'}))
    date_arrived = forms.DateField(label="Tanggal Kedatangan", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input partai', 'placeholder': 'yyyy-mm-dd'}))
    log_cost = forms.DecimalField(label="Log Cost", widget=forms.TextInput(attrs={'class': 'form-control partai'}))
    
    # species_id = forms.CharField(label="Species ID", widget=forms.TextInput(attrs={'class': 'form-control loglist'}))
    # log_colour = forms.CharField(label="Log Colour", widget=forms.TextInput(attrs={'class': 'form-control loglist'}))
    # log_length = forms.CharField(label="Log Length", widget=forms.TextInput(attrs={'class': 'form-control loglist'}))
    # diameter_1 = forms.CharField(label="Diameter 1", widget=forms.TextInput(attrs={'class': 'form-control loglist'}))
    # diameter_2 = forms.CharField(label="Diameter 2", widget=forms.TextInput(attrs={'class': 'form-control loglist'}))
    # average_diameter = forms.CharField(label="Average Diameter", widget=forms.TextInput(attrs={'class': 'form-control loglist'}))
    # volume_bruto = forms.CharField(label="Volume Bruto", widget=forms.TextInput(attrs={'class': 'form-control loglist'}))
    # volume_trimming = forms.CharField(label="Volume Trimming", widget=forms.TextInput(attrs={'class': 'form-control loglist'}))
    # volume_netto = forms.CharField(label="Volume Netto", widget=forms.TextInput(attrs={'class': 'form-control loglist'}))

    
    class Meta:
        model = Partai
        # fields = ['log_id','partai_id', 'tanggal_kedatangan', 'supplier_id', 'grade', 'species_id']
        fields = ['partai_id', 'supplier_id', 'date_arrived', 'log_cost']

        


class PartaiDataForm(forms.ModelForm):
    class Meta:
        model = Partai
        # fields = '__all__'
        fields = ['partai_id', 'supplier_id', 'date_arrived', 'log_cost']


class PartaiInputDataForm(forms.ModelForm):
    class Meta:
        model = Partai
        # fields = '__all__'
        fields = ['partai_id', 'supplier_id', 'date_arrived', 'log_cost']


    partai_id = forms.ModelChoiceField(queryset=Partai.objects.all())

    supplier_id = forms.ModelChoiceField(
        queryset=Supplier.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='supplier_id',  # Save only the 'supplier_id'
        empty_label="Select a supplier"
    )

    # species_id = forms.ModelChoiceField(
    #     queryset=Species.objects.all(),
    #     widget=forms.Select(attrs={'class': 'form-control'}),
    #     to_field_name='species_id',  # Save only the 'species_id'
    #     empty_label="Select a species"
    # )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the choices to display the concatenated value
        self.fields['supplier_id'].widget.choices = [
            (supplier.supplier_id, f"{supplier.supplier_id} - {supplier.supplier_name}")
            for supplier in Supplier.objects.all()
        ]
        # self.fields['species_id'].widget.choices = [
        #     (species.species_id, f"{species.species_id} - {species.species_name}")
        #     for species in Species.objects.all()
        # ]
    

    # class TransactionForm(forms.ModelForm):
    # bill_for = forms.CharField(label="Bill For", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))

    # issue_date = forms.DateField(label="Issue Date", widget=forms.DateInput(
    #     attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    # due_date = forms.DateField(label="Due Date", widget=forms.DateInput(
    #     attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    # total = forms.DecimalField(label="Total", max_digits=10, decimal_places=2,
    #                            widget=forms.TextInput(
    #                                attrs={'class': 'form-control transaction', 'placeholder': '...'}))

    # status = forms.CharField(label="Status", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))

    # class Meta:
    #     model = Transaction
    #     fields = ['bill_for', 'issue_date', 'due_date', 'total', 'status']

