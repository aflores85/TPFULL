from django.db import models
from questions.models import questions
from rest_framework import serializers

class answers(models.Model):
    code = models.CharField(max_length=10, unique=True)
    Name_answers = models.CharField(max_length=300, default='NUEVA_RESPUESTA')
    
    def __str__(self) -> str:
        return f'{self.Name_answers}'

    questions = models.ForeignKey(
        questions,
        related_name='answers',
        on_delete=models.DO_NOTHING,
        null=True
        )

    class Meta:
        verbose_name = "RESPUESTA"
        verbose_name_plural = "RESPUESTAS"
    
        
class answersSerializer(serializers.ModelSerializer):
        class Meta:
            model = answers
            fields = "__all__"

    