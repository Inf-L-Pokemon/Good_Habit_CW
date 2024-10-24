from rest_framework import generics

from habits.models import Habit
from habits.paginators import HabitPagination
from habits.serializers import HabitSerializer, HabitPublicSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('-id')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('-id')
    pagination_class = HabitPagination
    permission_classes = [IsOwner]


class HabitPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitPublicSerializer
    queryset = Habit.objects.filter(is_public=True).all().order_by('-id')
    pagination_class = HabitPagination


class HabitDetailAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
