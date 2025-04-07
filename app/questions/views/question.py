from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from questions.forms import AskQuestionForm
from questions.models import Question, Answer
from django.shortcuts import render, get_object_or_404
from django.views import View


class AskQuestionView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = AskQuestionForm
    template_name = "questions/ask_question.html"
    success_url = reverse_lazy("questions:home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionDetailView(View):
    template_name = "questions/question_detail.html"

    def get(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        answers = Answer.objects.filter(question=question).order_by("-created_at")
        return render(request, self.template_name, {"question": question, "answers": answers})