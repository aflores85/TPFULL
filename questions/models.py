
from django.db import models
from rest_framework import serializers
from subject.models import subject

class questions(models.Model):
    code = models.CharField(max_length=10, unique=True)
    Name_questions = models.CharField(max_length=300, default='NUEVA_PREGUNTA')
   
    def __str__(self) -> str:
        return f'{self.Name_questions}'

    subject = models.ForeignKey(
        subject,
        related_name='questions',
        on_delete=models.DO_NOTHING,
        null=True
        )

    class Meta:
           verbose_name = "PREGUNTA"
           verbose_name_plural = "PREGUNTAS"
    
        
class forumSerializer(serializers.ModelSerializer):
        class Meta:
            model = questions
            fields = "__all__"