from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com")
        self.habit = Habit.objects.create(
            place="дом",
            time="08:00:00",
            action="делать зарядку",
            is_pleasant_habit=False,
            frequency=1,
            award="съесть яблоко",
            execution_time=120,
            is_public=True,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        url = reverse('habits:habit-create')
        data = {
            "place": "дом",
            "time": "20:40:00",
            "action": "протереть пыль",
            "is_pleasant_habit": False,
            "frequency": 1,
            "award": "посмотреть фильм",
            "execution_time": 120,
            "is_public": True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_list(self):
        url = reverse("habits:habit-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_update(self):
        url = reverse("habits:habit-update", args=(self.habit.pk,))
        data = {
            "award": "посмотреть фильм",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("award"), "посмотреть фильм")

    def test_public_habit_list(self):
        url = reverse("habits:habit-public-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_delete(self):
        url = reverse("habits:habit-delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
