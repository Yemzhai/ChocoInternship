from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ObjectListMixin:
    model = None
    serializer = None

    def get(self, request):
        object = self.model.objects.all()
        serializer = self.serializer(object, many=True)
        return Response(serializer.data)


class ObjectDetailMixin:
    model = None
    serializer = None

    def get(self, request, pk):
        object = get_object_or_404(self.model, id=pk)
        serializer = self.serializer(object)
        return Response(serializer.data)
