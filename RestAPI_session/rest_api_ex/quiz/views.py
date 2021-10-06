from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random
# Create your views here.

@api_view(['GET'])
def helloAPI(request):
  return Response("hello world!")

# 랜덤 퀴즈를 id의 개수만큼 반환
@api_view(['GET'])
def randomQuiz(request, id):
  totalQuizs = Quiz.objects.all()
  randomQuizs = random.sample(list(totalQuizs), id) # json화가 되는 코드
  serializer = QuizSerializer(randomQuizs, many=True)
  return Response(serializer.data)