from django.db import models
from Forum.models import forum
from rest_framework import serializers

class discussion(models.Model):
    code = models.CharField(max_length=10, unique=True)
    Name_discussion = models.CharField(max_length=300, default='NUEVA_DISCUSION')
    
    def __str__(self) -> str:
        return f'{self.Name_discussion}'
    
    forum = models.ForeignKey(
        forum,
        related_name='discussion',
        on_delete=models.DO_NOTHING,
        null=True
        )

    class Meta:
        verbose_name = "DISCUSION"
        verbose_name_plural = "DISCUCIONES"

class discussionSerializer(serializers.ModelSerializer):
        class Meta:
            model = discussion
            fields = "__all__"