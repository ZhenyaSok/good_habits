from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from habits.models import Habit
from habits.pagination import PagePagination
from habits.serializers import HabitSerializer, HabitCreateSerializer, AdvisableHabitSerializer
from users.permissions import IsOwner


class HabitAllListAPIView(generics.ListAPIView):
    '''Список всех опубликованных привычек'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_published=True)
    permission_classes = [AllowAny]
    pagination_class = PagePagination


class HabitListAPIView(generics.ListAPIView):
    '''Список личных привычек'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = PagePagination
    permission_classes = [IsAuthenticated, IsOwner]

class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание привычки """
    serializer_class = HabitCreateSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()

class HabitRetrieveAPIView(generics.RetrieveAPIView):
    '''Просмотр деталей привычки'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner]

class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitAdvisableViewSet(viewsets.ModelViewSet):
    """ViewSet для приятных привычек """
    serializer_class = AdvisableHabitSerializer
    queryset = Habit.objects.filter(sign_of_pleasant_habit=True)
    permission_classes = [IsAuthenticated]


    def get_permissions(self):
        if self.action == 'CREATE':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, IsOwner]

        return super().get_permissions()

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()