from django.db import models
from django.contrib.auth.models import User
from questions.models.answer import Answer


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "answer")

    def __str__(self):
        return f"{self.user.username} liked answer {self.answer.id}"
