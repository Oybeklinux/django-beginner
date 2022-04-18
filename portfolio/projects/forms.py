from django import forms
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

        widgets = {
            'tag': forms.CheckboxSelectMultiple()
        }


    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})