from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.pagination import PagePagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateApiView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_subject = serializer.save()
        new_subject.owner = self.request.user
        new_subject.save()

class HabitListApiView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = PagePagination
    permission_classes = [IsAuthenticated, IsOwner]

class HabitRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

class HabitUpdateApiView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

class HabitDeleteApiView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]