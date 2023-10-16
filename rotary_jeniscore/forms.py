from django import forms
from .models import JenisCore
from django.db.models import F, Func



class JenisCoreInputForm(forms.ModelForm):
    id_jenis_core = forms.CharField(label="Jenis Core ID", widget=forms.TextInput(attrs={'class': 'form-control jeniscore'}))
    faktor_koreksi = forms.CharField(label="Faktor Koreksi", widget=forms.TextInput(attrs={'class': 'form-control jeniscore'}))

    class Meta:
        model = JenisCore
        fields = ['id_jenis_core', 'faktor_koreksi']

# class SawnLogInputForm(forms.ModelForm):

#     log_id = forms.CharField(label="Log ID", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
#     sawn_id = forms.CharField(label="Sawn ID", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
#     # jumlah_potong = forms.CharField(label="Jumlah potong", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))

#     class Meta:
#         model = SawnLog
#         fields = ['log_id', 'sawn_id']


# class SawnLogForm(forms.ModelForm):

#     log_id = forms.CharField(label="Log ID", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
#     sawn_id = forms.CharField(label="Sawn ID", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
#     sawn_length = forms.CharField(label="Sawn Length", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
#     diameter_1 = forms.CharField(label="Diameter 1", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
#     diameter_1= forms.CharField(label="Diameter 2", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
#     average_diameter = forms.CharField(label="Average Diameter", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
#     sawn_grade = forms.CharField(label="Sawn Grade", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
#     volume = forms.CharField(label="Volume", widget=forms.TextInput(attrs={'class': 'form-control sawnlog'}))
    
    
#     class Meta:
#         model = SawnLog
#         fields = ['log_id', 'sawn_id', 'sawn_length', 'diameter_1', 'diameter_2','average_diameter','sawn_grade','volume']

        

