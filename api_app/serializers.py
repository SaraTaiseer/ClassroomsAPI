from rest_framework import serializers

from classes.models import Classroom
from django.contrib.auth.models import User


class ListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject','name','year','teacher','id']

class DetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject','name','year','teacher','id']


class UpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject','name','year']

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields= ['subject','name','year','teacher']

# class UserCreateSerializer(serializers.ModelSerializer):
# 	password = serializers.CharField(write_only=True)
# 	class Meta:
# 		model = User
# 		fields = ['username', 'password']
#
# 	def create(self, validated_data):
# 		username = validated_data['username']
# 		password = validated_data['password']
# 		new_user = User(username=username)
# 		new_user.set_password(password)
# 		new_user.save()
# 		return validated_data
