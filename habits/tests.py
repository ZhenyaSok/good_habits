from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from habits.serializers import HabitSerializer, AdvisableHabitSerializer
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@ya.ru')
        self.habit = Habit.objects.create(owner=self.user, place='Тут', action='Живем', sign_of_pleasant_habit=True,
                                          is_published=True)  # приятная привычка
        self.client.force_authenticate(user=self.user)
        self.serializer_data = HabitSerializer([self.habit], many=True).data


    def test_get_list(self):
        """Тест просмотра списка своих привычек (list)"""

        response = self.client.get(reverse('habits:habit_list'))
        self.assertEqual(self.serializer_data, response.data.get('results'))
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_serializer_data(self):
        """Тест на сравнение нужных полей в отображении list через сериалайзер"""
        expected_data = [
            {
                'id': self.habit.pk,
                'place': 'Тут',
                'time': '12:00:00',
                'action': 'Живем',
                'sign_of_pleasant_habit': True,
                'periodicity': 1,
                'reward': None,
                'time_to_complete': None,
                'is_published': True,
                'owner': self.user.pk,
                'related_habit': None
            }
        ]

        self.assertEqual(expected_data, self.serializer_data)

    def test_create_habit(self):
        """Тест создания привычки (create)"""

        data = {

            "place": "Везде",
            "time": "12:00",
            "action": "Учиться",
            "sign_of_pleasant_habit": "False",
            "periodicity": "1",
            "reward": "",
            "time_to_complete": "2",
            "is_published": "True",
            "owner": 1,
            "related_habit": 1
        }

        response = self.client.post(
            reverse('habits:create_habit'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_retrieve_habit(self):
        """Тестирование вывода одной привычки"""

        response = self.client.get(
            reverse('habits:retrieve_habit', args=[self.habit.pk])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['action'], self.habit.action)

    def test_update_habit(self):
        """Тест обновления привычки"""
        data = {
            'place': 'ТАм'

        }

        response = self.client.patch(
            reverse('habits:update_habit', args=[self.habit.id]), data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['place'], data['place'])

    def test_get_all_list(self):
        """Тест просмотра списка всех опубликованных привычек (list)"""

        response = self.client.get(reverse('habits:list_all'))
        self.assertEqual(self.serializer_data, response.data.get('results'))
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )


    def test_delete_habit(self):
        """Тест удаления привычки"""
        response = self.client.delete(
            reverse('habits:destroy_habit', args=[self.habit.pk])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=self.habit.pk).exists())



class ViewSetsTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@yah.ru')
        self.habit = Habit.objects.create(owner=self.user, place='Там', action='Работаем', sign_of_pleasant_habit=True,
                                          is_published=True)  # приятная привычка
        self.client.force_authenticate(user=self.user)
        self.serializer_data_all = AdvisableHabitSerializer([self.habit], many=True).data


    def test_adv_list(self):
        """Тест на получение листа приятных привычек"""

        response = self.client.get(reverse('habits:advisable-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_serializer_adv(self):
        """Тест на сравнение нужных полей в отображении list приятных привычек, через сериалайзер"""
        expected_data = [
            {
                'id': self.habit.pk,
                'place': 'Там',
                'time': '12:00:00',
                'action': 'Работаем',
                'sign_of_pleasant_habit': True,
                'periodicity': 1,
                'time_to_complete': None,
                'is_published': True,
                'owner': self.user.pk
            }
        ]
        self.assertEqual(expected_data, self.serializer_data_all)
