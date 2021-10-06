from django.urls import path, include
from .views import *

urlpatterns = [
  path("hello/", helloAPI, name="helloAPI"),
  path("<int:id>/", randomQuiz, name="randomQuiz"), # 몇번째 퀴즈인지 식별하는 id
  
]