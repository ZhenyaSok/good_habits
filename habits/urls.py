from django.urls import path
from rest_framework import routers

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDestroyAPIView, \
    HabitRetrieveAPIView, HabitAllListAPIView, HabitAdvisableViewSet

app_name = HabitsConfig.name

urlpatterns = [
    path('list/', HabitListAPIView.as_view(), name='habit_list'),
    path('create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='destroy_habit'),
    path('retrieve/<int:pk>/', HabitRetrieveAPIView.as_view(), name='retrieve_habit'),

    path('list_all/', HabitAllListAPIView.as_view(), name='list_all'),
]

router = routers.SimpleRouter()
router.register(r'advisable', HabitAdvisableViewSet, basename='advisable')

urlpatterns += router.urls
