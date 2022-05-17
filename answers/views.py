from rest_framework import viewsets
from answers.models import answers
from answers.models import answersSerializer

class answersViewSet(viewsets.ModelViewSet):
    queryset = answers.objects.all().order_by("Name_answers")
    serializer_class = answersSerializer
