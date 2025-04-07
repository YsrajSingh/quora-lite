from django import forms
from questions.models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Write your answer..."}),
        }
