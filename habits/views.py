from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from habits.models import Habit
from habits.pagination import PagePagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitAllListApiView(generics.ListAPIView):
    '''Список всех опубликованных привычек'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [AllowAny]
    pagination_class = PagePagination


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

class HabitDestroyApiView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]