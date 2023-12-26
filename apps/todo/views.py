from datetime import datetime

from django.db import transaction
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from todo.models import ToDoWoo
from todo.serializers import TodoWooModelSerializer, TodoSerializer


class TodoViewSet(CreateModelMixin, GenericViewSet):
    queryset = ToDoWoo.objects.all()
    serializer_class = TodoWooModelSerializer
    permission_classes = (IsAuthenticated,)

    @action(['get'], False, 'current')
    def get_todos(self, request):
        todos = ToDoWoo.objects.filter(author=request.user, is_complete=False)
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)

    @action(['get'], True)
    def complete(self, request, pk):
        try:
            with transaction.atomic():
                todo = get_object_or_404(ToDoWoo, pk=pk, author=request.user, is_complete=False)
                todo.is_complete = True
                todo.completed_at = datetime.now()
                todo.save()
                context = {'message': 'Success'}
                return Response(context)
        except Exception:
            context = {'message': "Todo complete bo'lgan yoki sizga tegishli emas"}
            return Response(context, 400)

    @action(['get'], False, url_path='completed', serializer_class=TodoSerializer)
    def get_completed(self, request):
        todos = ToDoWoo.objects.filter(author=request.user, is_complete=True)
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)

    @action(['delete'], True, url_path='del')
    def delete_todo(self, request, pk):
        try:
            with transaction.atomic():
                todo = get_object_or_404(ToDoWoo, pk=pk, author=request.user)
                todo.delete()
            context = {'message': 'Success'}
            return Response(context, 204)
        except Exception:
            context = {'message': "Allaqachon o'chirilgan yoki sizga tegishli emas !"}
            return Response(context, 400)
