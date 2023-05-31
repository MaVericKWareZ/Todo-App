import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.response import Response

from todo_app.general.permissions import IsObjectCreatorOrReadOnly
from todo_app.task.filters.task import TaskFilter
from todo_app.task.models import Task
from todo_app.task.serializers.task import TaskReadSerializer, TaskWriteSerializer

logger = logging.getLogger(__name__)


class TaskViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [IsObjectCreatorOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskWriteSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            task = serializer.save()
            read_serializer = TaskReadSerializer(task)
            logger.info(f'created task {read_serializer.data}')
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error('Error while creating task')
            return Response({'error_message': e.__str__()}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Task.objects.select_related('creator').order_by('-modified_date')

    def get_serializer_class(self):
        if self.action in ['create', 'partial_update', 'update']:
            return TaskWriteSerializer
        return TaskReadSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, context={'request': request}, partial=partial)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        read_serializer = TaskReadSerializer(task)
        return Response(read_serializer.data)
