from quizz.models import *
from rest_framework import viewsets,mixins,permissions
from quizz.Serializers import *
from django.shortcuts import render, get_object_or_404
from quizz.permissions import *
# Create your views here.
class QuizzViewSet(viewsets.ModelViewSet):

    serializer_class = QuizzSerializer

    def get_queryset(self):
        user=self.request.user
        student=get_object_or_404(Student,user=user)
        course=student.enrolled.all()
        qs1=Quizz.objects.filter(course_exam__in=course)
        return qs1

class AttendeesViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeesSerializer
    permission_classes = [adminuser]

class FacultysViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultysSerializer
    permission_classes = [adminuser]

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentsSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class= ChoiceSerializer