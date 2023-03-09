from tasks.models import Task
from tasks.serializers import TaskSerializer
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView

# Create your views here.
class HomeView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # def get_queryset(self):
    #     return Task.objects.filter(complete=False)
    
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = TaskSerializer(queryset, many=True)
    #     return JsonResponse(serializer.data)