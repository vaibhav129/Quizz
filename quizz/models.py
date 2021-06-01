from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    dept_code = models.CharField(max_length=3, unique=True)
    dept_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name

class Course(models.Model):
    course_code = models.CharField(max_length=6, unique=True)
    course_name = models.CharField(max_length=50)
    dept_key = models.ForeignKey(Department, on_delete=models.CASCADE)
    desc = models.TextField('Course Description',max_length=300,null=True,blank=True)

    def __str__(self):
        return self.course_name

class Faculty(models.Model):
    user = models.OneToOneField(User, related_name='faculty_user', on_delete=models.CASCADE, unique=True)
    course_faculty = models.ManyToManyField(Course)
    dept_faculty = models.ForeignKey('Department', on_delete=models.PROTECT)
    no = models.CharField(max_length=10)
    created = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.user.username}"


class Student(models.Model):
    user = models.OneToOneField(User, related_name='student_user', on_delete=models.CASCADE, unique=True)
    enrolled = models.ManyToManyField(Course)
    deptstud = models.ForeignKey('Department', on_delete=models.DO_NOTHING)
    bd = models.DateField(null=True, blank=True)
    no = models.CharField(max_length=10, unique=True, help_text='10-digit phone number')
    joined = models.DateField(null=True, blank=True)



class Quizz(models.Model):
    title = models.CharField(max_length=40, unique=True)
    course_exam = models.ForeignKey(Course, verbose_name='Course', on_delete=models.CASCADE,blank=True)
    total_marks = models.IntegerField(default=4, null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    time_limit = models.DurationField(help_text='HH:MM:SS format')
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,blank=True)
    text = models.TextField('Question Description',max_length=200)
    imageq = models.ImageField('Question Image', null=True, blank=True)

    def __str__(self):
        return self.title
class Choice(models.Model):
    question = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_selected = models.BooleanField('Selected Answer', default=False, null=True, blank=True)
    is_correct = models.BooleanField('Correct Answer', default=False)

class Attendee(models.Model):
    info = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    studenta = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.IntegerField(null=True, blank=True)
    submitted = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    marked = models.ForeignKey('Choice', on_delete=models.SET_NULL, blank=True, null=True)

def recent(self):
        return self.studenta

