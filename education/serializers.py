from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from education.models import Course, Lesson, Subscription
from education.validators import UrlValidator


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field="video_url")]


class CourseSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, course):
        return course.Уроки.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'lessons_count', 'lessons')


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"




