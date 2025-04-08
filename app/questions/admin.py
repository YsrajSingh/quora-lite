from django.contrib import admin
from questions.models.question import Question
from questions.models.answer import Answer
from questions.models.like import Like

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "created_at")
    search_fields = ("question__title", "content")

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "answer", "user", "created_at")
    search_fields = ("answer__content", "user__username")
