from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from questions.models import Question
from questions.forms.answer import AnswerForm

class PostAnswerView(LoginRequiredMixin, View):
    template_name = "answers/post_answer.html"

    def get(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        form = AnswerForm()
        return render(request, self.template_name, {"form": form, "question": question})

    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect("questions:question_detail", question_id=question.id)

        return render(request, self.template_name, {"form": form, "question": question})
