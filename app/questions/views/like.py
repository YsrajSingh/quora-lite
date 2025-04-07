from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View
from questions.models.answer import Answer
from questions.models.like import Like

@method_decorator(login_required, name="dispatch")
class LikeAnswerView(View):
    def post(self, request, answer_id):
        answer = get_object_or_404(Answer, id=answer_id)

        like, created = Like.objects.get_or_create(user=request.user, answer=answer)

        if not created:
            like.delete()  # Unlike if already liked

        return redirect("questions:home")
