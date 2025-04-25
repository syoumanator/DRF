from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from education.models import Course, Lesson
from education.validators import validate_url


class LessonSerializer(ModelSerializer):
    video_url = serializers.URLField(validators=[validate_url])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, course):
        return course.Уроки.count()


    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'lessons_count', 'lessons')




