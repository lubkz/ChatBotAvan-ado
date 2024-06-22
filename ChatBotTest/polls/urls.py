from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Esta linha corresponde à URL 'polls/'
    path('chatbot/', views.chatbot_response, name='chatbot_response'),
    path('test_form/', views.test_form, name='test_form'),
]
