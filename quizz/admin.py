from django.contrib import admin
from quizz.models import *
from .forms import *
# Register your models here.
class ChoiceInline(admin.TabularInline):
    extra = 0
    model = Choice
    form = ChoiceForm
class QuizzAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Quizz,QuizzAdmin)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Attendee)
admin.site.register(Course)
admin.site.register(Department)



