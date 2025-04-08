from django import forms
from questions.models import Question


class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }
