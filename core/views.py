from rest_framework import generics, status
from .models import Task, Activity, Loan
from .serializers import TaskSerializer, ActivitySerializer, LoanSerializer
from rest_framework import mixins
from rest_framework.response import Response
from django.http import Http404



class TasksList(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    search_fields = ['customer', 'status']
    ordering_fields = ['assigned_to', 'customer']
    ordering = ['assigned_to', 'customer']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class TaskDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TaskSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TaskSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActivityList(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    search_fields = ['status']
    ordering_fields = ['status']
    ordering = ['status']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ActivityDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ActivitySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ActivitySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class LoanList(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    search_fields = ['loan_account_number', 'customer', 'asset']
    ordering_fields = ['status', 'loan_account_number']
    ordering = ['status', 'loan_account_number']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class LoanDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_object(self, pk):
        try:
            return Loan.objects.get(pk=pk)
        except Loan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LoanSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LoanSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)