from tasks.models import Task
from tasks.serializers import TaskSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView

# Create your views here.
class HomeView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        qs = None
        if len(request.get_full_path().split('=')) == 2:
            if request.get_full_path().split('=')[1] == 'False':
                qs = Task.objects.filter(complete=False)
            else:
                qs = Task.objects.filter(complete=True)

        qs = Task.objects.all() if qs is None else qs
        return Response(
            data=self.serializer_class(qs, many=True).data,
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            data["title"] = data['title'].capitalize()
        except:
            return Response(
                {"title" : "please provide the title field"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().post(request, *args, **kwargs)
