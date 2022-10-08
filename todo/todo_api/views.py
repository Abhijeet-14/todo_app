
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import logging
logger = logging.getLogger(__name__)

# Create your views here.
class AddTask(APIView):

    def post(self, request):
        """Add new task"""
        err_ref = uuid.uuid4()
        try:
            logger.info("Enter: Add New Task")
            logger.info(request.data)

            logger.info("info logger")
            logger.debug("debug logger")
            logger.warn("warning logger")
            logger.error("error logger")
            logger.critical("critical logger")

            val = 1/0

            result = {
                "result": "Test_Result",
                "isTrue": True
            }

            logger.info("Exit: Add New Task")
            return Response(result, status=status.HTTP_200_OK)
        except Exception as err:
            logger.error(f"Exit : Error occured : {str(err)} :: err_ref : {err_ref}")
            return Response(
                {
                    "message": str(err), 
                    "isTrue": False,
                    "err_ref": err_ref
                }, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
