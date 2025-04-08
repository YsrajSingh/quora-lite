from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from questions.models import Question, Answer
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


class UpdateAnswerView(LoginRequiredMixin, View):
    template_name = "answers/post_answer.html"

    def get(self, request, answer_id):
        answer = get_object_or_404(Answer, id=answer_id, author=request.user)
        form = AnswerForm(instance=answer)
        return render(
            request, self.template_name, {"form": form, "question": answer.question}
        )

    def post(self, request, answer_id):
        answer = get_object_or_404(Answer, id=answer_id, author=request.user)
        form = AnswerForm(request.POST, instance=answer)

        if form.is_valid():
            form.save()
            return redirect("questions:question_detail", question_id=answer.question.id)

        return render(
            request, self.template_name, {"form": form, "question": answer.question}
        )


class DeleteAnswerView(LoginRequiredMixin, View):
    template_name = "answers/confirm_delete.html"

    def get(self, request, answer_id):
        answer = get_object_or_404(Answer, id=answer_id, author=request.user)
        return render(request, self.template_name, {"answer": answer})

    def post(self, request, answer_id):
        answer = get_object_or_404(Answer, id=answer_id, author=request.user)
        question_id = answer.question.id
        answer.delete()
        return redirect("questions:question_detail", question_id=question_id)
