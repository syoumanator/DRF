from rest_framework.serializers import ModelSerializer, SerializerMethodField

from education.models import Course, Lesson


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()

    def get_lessons_count(self, course):
        return course.Уроки.count()

    class Meta:
        model = Course
        fields = ('title', 'preview', 'description', 'lessons_count')

