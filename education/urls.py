from django.urls import path

from education.apps import EducationConfig
from rest_framework.routers import DefaultRouter

from education.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-get"),
    path("lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path("lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson-delete"),
] + router.urls

