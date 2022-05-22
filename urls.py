from django.db import router
from django.urls import URLPattern
from rest_framework import routers
from answers.views import answersViewSet

router = routers.DefaultRouter()
router.register(r"answers", answersViewSet, "answers")
router.register(r"discussion", answersViewSet, "discussion")
router.register(r"Forum", answersViewSet, "Forum")
router.register(r"questions", answersViewSet, "questions")
router.register(r"subject", answersViewSet, "subject")


URLPattern = router.urls 

