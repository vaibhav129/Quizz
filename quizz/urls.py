from rest_framework import routers
from quizz.views import *
from . import views
from django.urls import include,path
router = routers.SimpleRouter()
router.register(r"quizz",QuizzViewSet,basename='quizz')
router.register(r"Courses",CoursesViewSet)
router.register(r"attendess", AttendeesViewSet)
router.register(r"departments", DepartmentsViewSet)
router.register(r"faculty", FacultysViewSet)
router.register(r"student", StudentsViewSet)
router.register(r"choice", ChoiceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]