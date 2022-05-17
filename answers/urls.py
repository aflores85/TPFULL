from django.db import router
from rest_framework import routers
from answers.views import answersViewSet

router = routers.DefaultRouter()
router.register(r"answers", answersViewSet, "answers")

