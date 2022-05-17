from django.db import models
from rest_framework import serializers
from discussion.models import discussion

class subject(models.Model):
    code = models.CharField(max_length=10, unique=True)
    Name_subject = models.CharField(max_length=300, default='NUEVO_TEMA')

    def __str__(self) -> str:
        return f'{self.Name_subject}'

    discussion = models.ForeignKey(
        discussion,
        related_name='subject',
        on_delete=models.DO_NOTHING,
        null=True
        )

    class Meta:
        verbose_name = "TEMA"
        verbose_name_plural = "TEMAS"

class subjectSerializer(serializers.ModelSerializer):
        class Meta:
            model = subject
            fields = "__all__"