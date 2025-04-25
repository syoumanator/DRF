from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from education.models import Course, Lesson, Subscription
from education.validators import UrlValidator


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field="video_url")]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    subscription = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        # fields = ('id', 'title', 'preview', 'description', 'lessons_count', 'lessons')
        fields = "__all__"

    def get_lessons_count(self, course):
        return course.Уроки.count()

    def get_subscription(self, instance):
        user = self.context["request"].user
        return Subscription.objects.filter(user=user).filter(course=instance).exists()




