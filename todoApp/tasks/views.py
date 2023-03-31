from tasks.models import Task
from tasks.serializers import TaskSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class ListCreateTaskView(ListCreateAPIView):
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

class UpdateDestroyTaskView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            task = Task.objects.get(pk=kwargs['pk'])
            return Response(TaskSerializer(task).data)
        except:
            return Response(
                {"404_Not_Found": f"Task with pk: {kwargs['pk']} not found."},
                status.HTTP_404_NOT_FOUND
                )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = {
            "title": request.data.get('title', None),
        }
        serializer = TaskSerializer(instance=instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance=instance)
        except status.HTTP_404_NOT_FOUND:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
