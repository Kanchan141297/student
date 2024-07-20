from rest_framework import serializers
from serialize_app.models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rollno = serializers.IntegerField()
    name = serializers.CharField()
    school = serializers.CharField(write_only=True)
    marks = serializers.DecimalField(max_digits=5 ,decimal_places=2)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)