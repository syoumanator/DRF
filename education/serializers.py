from rest_framework.serializers import ModelSerializer, SerializerMethodField

from education.models import Course, Lesson


class LessonSerializer(ModelSerializer):

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




