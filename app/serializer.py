from rest_framework import serializers
from .models import Batch
from django.contrib.auth.models import User


    
   
class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Batch
        fields="__all__"

# serializers.py
from rest_framework import serializers
from .models import AddStudent

class AddStudentSerializer(serializers.ModelSerializer):
    student_username = serializers.ReadOnlyField(source='stud.username')
    batchname=serializers.ReadOnlyField(source='batch.batch_name')
    class Meta:
        model = AddStudent
        fields = '__all__'


from rest_framework import serializers
from .models import Student, WaitingList

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ["id","username","password","gender","dob","phone","full_name","selected_course"]

class WaitingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingList
        fields = '__all__'


