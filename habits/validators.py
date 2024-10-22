from rest_framework.serializers import ValidationError


class PleasantHabitOrAward:
    """Исключает одновременный выбор приятной привычки и вознаграждения."""

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        val_1 = value.get(self.field_1)
        val_2 = value.get(self.field_2)
        if val_1 and val_2:
            raise ValidationError(
                'Нельзя одновременно указывать и приятную привычку и вознаграждение. Пожалуйста, выберите что-нибудь '
                'одно.')


class ExecutionTime:
    """Проверяет время выполнения привычки, которое должно быть больше 120 секунд."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = value.get(self.field)
        if val and val > 120:
            raise ValidationError('Время выполнения привычки должно быть не более 120 секунд.')


class PleasantHabit:
    """Проверяет, что в связанные привычки попадают только приятные привычки."""

    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, value):
        val = value.get(self.field_1)
        if val:
            if not val.is_pleasant_habit:
                raise ValidationError('Полезную привычку можно связать только с приятной привычкой.')


class PleasantHabitNotHaveAwardOrPleasantHabit:
    """Проверяет приятную привычку на отсутствие вознаграждения или связанной приятной привычки"""

    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        val_1 = value.get(self.field_1)
        val_2 = value.get(self.field_2)
        val_3 = value.get(self.field_3)
        if val_1:
            if val_2 is not None or val_3 is not None:
                raise ValidationError(
                    'Приятная привычка не может иметь вознаграждение или связанную приятную привычку.')


class Frequency:
    """Проверяет периодичность выполнения привычки, должна быть менее 8 дней"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = value.get(self.field)
        if val and val > 7:
            raise ValidationError('Периодичность выполнения привычки должна быть менее 8 дней.')
