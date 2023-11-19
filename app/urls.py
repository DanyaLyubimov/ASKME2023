from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('question/<int:question_id>', views.question, name="question"),
    path('login', views.authorization, name="authorization"),
    path('ask', views.new_question, name="new_question"),
    path('my_profile', views.my_profile, name="my_profile"),
    path('signup', views.registration, name="registration"),
    path('hot', views.hot_questions, name="hot_questions"),
    path('tag/<str:tag_name>/', views.tag_questions, name="tag_questions"),
]
