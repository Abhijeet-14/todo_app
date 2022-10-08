
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class AddTask(APIView):

    def post(self, request):
        """Add new task"""
        print("Enter: Add New Task")
        print(request.data)
        result = {
            "result": "Test_Result",
            "isTrue": True
        }

        return Response(result, status=status.HTTP_200_OK)