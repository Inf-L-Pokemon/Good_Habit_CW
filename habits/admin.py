from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('action', 'owner', 'is_pleasant_habit', 'frequency', 'award', 'is_public')
    search_fields = ('action', 'owner', 'is_pleasant_habit', 'award', 'is_public')
