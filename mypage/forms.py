from django import forms
from .models import *
from lecturelist.models import Lecuture

class FundingForm(forms.ModelForm):
    lecture_title = forms.CharField(label='강의 제목', widget=forms.Textarea(
        attrs={'name': 'funding_title'}))
    lecture_summary = forms.CharField(label='강의 요약', widget=forms.Textarea(
        attrs={'rows': 10, 'cols': 100, 'maxlength': 500, 'id': "txt2", 'name': 'funding_summary'}))

    class Meta:
        model = Lecuture
        fields = ['lecture_title', 'lecture_summary']