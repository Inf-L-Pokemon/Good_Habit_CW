from rest_framework import serializers

from habits.models import Habit
from habits.validators import PleasantHabitOrAward, ExecutionTime, PleasantHabit, \
    PleasantHabitNotHaveAwardOrPleasantHabit, Frequency


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            PleasantHabitOrAward('pleasant_habit', 'award'),
            ExecutionTime('execution_time'),
            PleasantHabit('pleasant_habit'),
            PleasantHabitNotHaveAwardOrPleasantHabit('is_pleasant_habit', 'award', 'pleasant_habit'),
            Frequency('frequency')
        ]


class HabitPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('action', 'place', 'time', 'pleasant_habit', 'award',)
