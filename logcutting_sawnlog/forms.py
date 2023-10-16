from django import forms
from .models import SawnLog, SawnLogInput
from django.db.models import F, Func



class SawnLogInputForm(forms.ModelForm):

    log_id = forms.CharField(label="Log ID", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    sawn_id = forms.CharField(label="Sawn ID", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    

    class Meta:
        model = SawnLogInput
        fields = ['sawn_id','log_id','sawn_length', 'sawn_grade' ,'diameter_1', 'diameter_2','average_diameter','volume']

    sawn_length = forms.IntegerField(required=False)
    sawn_grade = forms.CharField(required=False)
    diameter_1 = forms.IntegerField(required=False)
    diameter_2 = forms.IntegerField(required=False)
    average_diameter = forms.IntegerField(required=False)
    volume = forms.IntegerField(required=False)



class SawnLogForm(forms.ModelForm):

    # sawn_id = forms.CharField(label="Sawn ID", widget=forms.TextInput(attrs={'class': 'form-control sawnlog','disabled': True}))
    # log_id = forms.CharField(label="Log ID", widget=forms.TextInput(attrs={'class': 'form-control sawnlog','disabled': True}))
    sawn_length = forms.CharField(label="Sawn Length", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    sawn_grade = forms.CharField(label="Sawn Grade", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    diameter_1 = forms.CharField(label="Diameter 1", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    diameter_2= forms.CharField(label="Diameter 2", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    average_diameter = forms.CharField(label="Average Diameter", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    volume = forms.CharField(label="Volume", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    
    
    class Meta:
        model = SawnLog
        fields = ['sawn_length', 'sawn_grade' ,'diameter_1', 'diameter_2','average_diameter','volume']
        # fields = ['sawn_id','log_id','sawn_length', 'sawn_grade' ,'diameter_1', 'diameter_2','average_diameter','volume']


class SawnLogEditForm(forms.ModelForm):

    sawn_id = forms.CharField(label="Sawn ID", widget=forms.TextInput(attrs={'class': 'form-control sawnlog','disabled': True}))
    log_id = forms.CharField(label="Log ID", widget=forms.TextInput(attrs={'class': 'form-control sawnlog','disabled': True}))
    sawn_length = forms.CharField(label="Sawn Length", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    sawn_grade = forms.CharField(label="Sawn Grade", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    diameter_1 = forms.CharField(label="Diameter 1", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    diameter_2= forms.CharField(label="Diameter 2", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    
    
    class Meta:
        model = SawnLog
        fields = ['sawn_id','log_id','sawn_length', 'sawn_grade' ,'diameter_1', 'diameter_2']
        # fields = ['sawn_id','log_id','sawn_length', 'sawn_grade' ,'diameter_1', 'diameter_2','average_diameter','volume']

        

