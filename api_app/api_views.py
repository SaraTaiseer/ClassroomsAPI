from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from classes.models import Classroom
from .serializers import ListSerializer,DetailsSerializer,UpdateSerializer,CreateSerializer


class APIListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ListSerializer


class classroomDetails(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = DetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class UpdateClassroom(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class CancelClassroom(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class classroomCreate(CreateAPIView):
	serializer_class = CreateSerializer

	def perform_create(self, serializer):
		# teacher_id=self.kwargs.get("teacher_id")
		# teacher_object=Classroom.objects.get(id=teacher_id)
		serializer.save(teacher=self.request.user)
		# classroom=teacher_object ,

# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserCreateSerializer
