
from django.db import models
from rest_framework import serializers


class forum(models.Model):
    code = models.CharField(max_length=10, unique=True)
    Name_forum = models.CharField(max_length=300, default='NUEVO_FORO')
  
    def __str__(self) -> str:
     return f'{self.Name_forum}'

    class Meta:
        verbose_name = "FORO"
        verbose_name_plural = "FOROS"
    
        
class forumSerializer(serializers.ModelSerializer):
        class Meta:
            model = forum
            fields = "__all__"

