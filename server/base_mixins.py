from rest_framework import status
from rest_framework.response import Response


class DestroyModelMixin:
    """Soft deletion объекта."""

    def destroy(self, request, *args, **kwargs):
        """Помечаем на удаление объект."""
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    