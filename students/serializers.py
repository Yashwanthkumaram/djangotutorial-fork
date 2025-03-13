from rest_framework import serializers
from .models import Student, Subject, Result

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

   

class SubjectSerializer(serializers.ModelSerializer):
    std = StudentSerializer() 

    class Meta:
        model = Subject
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    student = StudentSerializer()  
    subject = SubjectSerializer()  

    class Meta:
        model = Result
        fields = '__all__'

    def validate_sem(self, value):
        """
        Check that the blog post is about Django.
        """
        if not (value>0 and value<8):
            raise serializers.ValidationError("Sem value is beyond Imaginations")
        return value
