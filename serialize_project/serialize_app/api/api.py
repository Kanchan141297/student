from rest_framework.views import APIView
from rest_framework.response import Response
from serialize_app.models import Student
from .serializers import StudentSerializer

class StudentAPI(APIView):

    def get(self,request):
        querySet = Student.objects.all()
        serializer = StudentSerializer(querySet , many=True)
        return Response(data=serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)












