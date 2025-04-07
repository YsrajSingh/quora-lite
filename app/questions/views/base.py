# questions/views/base.py

from django.views.generic import ListView
from questions.models import Question

class HomeView(ListView):
    model = Question
    template_name = "home.html"
    context_object_name = "questions"
    ordering = ["-created_at"]

