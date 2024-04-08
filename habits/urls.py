from django.urls import path

from habits.views import HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDestroyAPIView, \
    HabitRetrieveAPIView, HabitAllListAPIView

urlpatterns = [
    path('list/', HabitListAPIView.as_view(), name='habit_list'),
    path('create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('update/', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('delete/', HabitDestroyAPIView.as_view(), name='destroy_habit'),
    path('retrieve/', HabitRetrieveAPIView.as_view(), name='retrieve_habit'),

    path('list_all/', HabitAllListAPIView.as_view(), name='list_all'),
]