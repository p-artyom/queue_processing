from api.tasks import processing_command_task
from celery import uuid
from django.http import HttpRequest, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def processing_command(request: HttpRequest) -> HttpResponse:
    task_id = uuid()
    processing_command_task.apply_async(
        (request.data['command'],),
        task_id=task_id,
    )
    return Response(
        {
            'task_id': (task_id),
        },
        status=status.HTTP_200_OK,
    )
