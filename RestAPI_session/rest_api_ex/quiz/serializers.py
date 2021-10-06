## django의 모델 데이터를 json으로 만들어주는 파일
from django.db import models
from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
  class Meta:
    model = Quiz
    fields = ('title', 'body', 'answer')