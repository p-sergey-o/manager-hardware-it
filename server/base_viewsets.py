from rest_framework import mixins
from rest_framework import viewsets

from server import base_mixins


class BaseModelViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       base_mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    """Базовый набор представлений"""

    pass
