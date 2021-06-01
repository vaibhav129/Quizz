from rest_framework import serializers
from quizz.models import *

class  ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Choice
        fields = '__all__'

class  QuizzSerializer(serializers.ModelSerializer):
    choice_set= ChoiceSerializer(many=True)
    class Meta:
        model= Quizz
        fields = '__all__'
class  DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Department
        fields = '__all__'

class  CoursesSerializer(serializers.ModelSerializer):
    dept_key=DepartmentsSerializer()
    class Meta:
        model= Course
        fields = '__all__'


class  FacultysSerializer(serializers.ModelSerializer):
    course_faculty =CoursesSerializer(many=True)
    dept_faculty =DepartmentsSerializer()
    class Meta:
        model= Faculty
        fields = '__all__'

class  AttendeesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Attendee
        fields = '__all__'

class  StudentsSerializer(serializers.ModelSerializer):
    enrolled=CoursesSerializer(many=True)
    deptstud=DepartmentsSerializer()
    class Meta:
        model= Student
        fields = '__all__'


