from django.urls import path

from habits.views import HabitListApiView, HabitRetrieveApiView, HabitDestroyApiView, HabitUpdateApiView, \
    HabitCreateApiView

urlpatterns = [
    path('list/', HabitListApiView.as_view(), name='habit_list'),
    path('create/', HabitCreateApiView.as_view(), name='create_habit'),
    path('update/', HabitUpdateApiView.as_view(), name='update_habit'),
    path('delete/', HabitDestroyApiView.as_view(), name='destroy_habit'),
    path('retrieve/', HabitRetrieveApiView.as_view(), name='retrieve_habit'),
]