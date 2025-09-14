from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lessons_in_course = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source="lesson_set")

    def get_lessons_in_course(self, course):
        return course.lesson_set.all().count()

    def get_lessons(self, course):
        return course.lesson_set.all()

    class Meta:
        model = Course
        fields = ("name", "description", "lessons_in_course", "lessons")
