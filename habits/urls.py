from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitDetailAPIView, HabitListAPIView, HabitPublicListAPIView, \
    HabitUpdateAPIView, HabitDeleteAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('', HabitListAPIView.as_view(), name='habit-list'),
    path('public/', HabitPublicListAPIView.as_view(), name='habit-public-list'),
    path('<int:pk>/', HabitDetailAPIView.as_view(), name='habit-detail'),
    path('<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('<int:pk>/delete/', HabitDeleteAPIView.as_view(), name='habit-delete'),
]
