# questions/urls.py

from django.urls import path
from questions.views import auth, question, answer, like, base

app_name = "questions"

urlpatterns = [
    # Auth
    path("login/", auth.LoginView.as_view(), name="login"),
    path("register/", auth.RegisterView.as_view(), name="register"),
    path("logout/", auth.logout_view, name="logout"),
    # # Home / Base
    path("", base.HomeView.as_view(), name="home"),
    # # Questions
    path("ask/", question.AskQuestionView.as_view(), name="ask_question"),
    path(
        "question/<int:question_id>/",
        question.QuestionDetailView.as_view(),
        name="question_detail",
    ),
    # # Answers
    path(
        "answer/<int:question_id>/",
        answer.PostAnswerView.as_view(),
        name="answer_question",
    ),
    path(
        "answer/<int:question_id>/edit/",
        answer.UpdateAnswerView.as_view(),
        name="edit_answer",
    ),
    path(
        "answer/<int:question_id>/delete/",
        answer.DeleteAnswerView.as_view(),
        name="delete_answer",
    ),
    # # Likes
    path("like/<int:answer_id>/", like.LikeAnswerView.as_view(), name="like_answer"),
]
