from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit, PleasantHabit
from users.models import User


# Create your tests here.


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            telegram='testtg',
            is_superuser=True,
            is_active=True,
            is_staff=True,
        )

        self.user.set_password('123456')
        self.user.save()

        self.habit = Habit.objects.create(
            place='test_place',
            time='14:30',
            action='test_action',
            estimated_time=30,

        )

        self.pleasant_habit = PleasantHabit.objects.create(
            place='test_place1',
            time='14:30',
            action='test_action1',
            estimated_time=40,
        )

        response = self.client.post('/users/login/', {'telegram': 'testtg', 'password': '123456'})
        token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_get_list(self):
        """ Test for getting list of habits """

        response = self.client.get(
            reverse('habits:habits_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {'id': self.pleasant_habit.id,
                     'user': None,
                     'place': 'test_place',
                     'time': '14:30:00',
                     'action': 'test_action',
                     'connected_habit': None,
                     'periodicity': 1,
                     'reward': None,
                     'estimated_time': 30,
                     'is_public': True}
                ]
            }
        )

    def test_post_create(self):
        """ Test for creating new habit """

        data = {
            'place': 'test_place2',
            'time': '14:30',
            'action': 'test_action2',
            'estimated_time': 30
        }

        response = self.client.post(
            '/habits/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_habit_update(self):
        """ Test for patching habit """

        data = {
            'place': 'test_place3',
            'time': '14:30',
            'action': 'test_action3',
            'estimated_time': 30
        }

        response = self.client.put(
            reverse('habits:habit_update', args=[self.habit.id]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_habit_destroy(self):
        self.client.delete(
            reverse('habits:habit_destroy', args=[self.habit.id])
        )

        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())


class PleasantHabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            telegram='testtg',
            is_superuser=True,
            is_active=True,
            is_staff=True,
        )

        self.user.set_password('123456')
        self.user.save()

        self.habit = Habit.objects.create(
            place='test_place',
            time='14:30',
            action='test_action',
            estimated_time=30,

        )

        self.pleasant_habit = PleasantHabit.objects.create(
            place='test_place1',
            time='14:30',
            action='test_action1',
            estimated_time=40,
        )

        response = self.client.post('/users/login/', {'telegram': 'testtg', 'password': '123456'})
        token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_get_list_pleasant(self):
        """ Test for getting list of habits """

        response = self.client.get(
            '/pleasant_habits/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {'id': self.pleasant_habit.id,
                     'user': None,
                     'place': 'test_place1',
                     'time': '14:30:00',
                     'action': 'test_action1',
                     'periodicity': 1,
                     'estimated_time': 40,
                     'is_public': True}
                ]
            }
        )

    def test_get_list_public(self):
        """ Test for getting list of habits """

        response = self.client.get(
            reverse('habits:public_habits_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {'id': self.pleasant_habit.id,
                     'user': None,
                     'place': 'test_place1',
                     'time': '14:30:00',
                     'action': 'test_action1',
                     'periodicity': 1,
                     'estimated_time': 40,
                     'is_public': True}
                ]
            }
        )

    def test_post_create_pleasant(self):
        """ Test for creating new habit """

        data = {
            'place': 'test_place2',
            'time': '14:30',
            'action': 'test_action2',
            'estimated_time': 30
        }

        response = self.client.post(
            '/pleasant_habits/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_pleasant_habit_update(self):
        """ Test for patching habit """

        data = {
            'place': 'test_place3',
            'time': '14:30',
            'periodicity': 1,
            'action': 'test_action3',
            'estimated_time': 30
        }

        response = self.client.patch(
            f'/pleasant_habits/{self.pleasant_habit.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_pleasant_habit_destroy(self):
        self.client.delete(
            f'/pleasant_habits/{self.pleasant_habit.id}/'
        )

        self.assertFalse(PleasantHabit.objects.filter(id=self.pleasant_habit.id).exists())
