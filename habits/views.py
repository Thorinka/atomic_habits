from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from habits.models import Habit, PleasantHabit
from habits.paginators import HabitsPaginator, PleasantHabitsPaginator, PleasantHabitsPublicPaginator
from habits.permissions import IsOwner, IsModerator
from habits.serializers import HabitSerializer, PleasantHabitSerializer
from users.models import UserRoles


class PleasantHabitViewSet(viewsets.ModelViewSet):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all().order_by('id')
    permission_classes = [IsAuthenticated]
    pagination_class = PleasantHabitsPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('user', 'is_public',)
    ordering_fields = ('id', 'action',)

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.role == UserRoles.MODERATOR:
            return PleasantHabit.objects.all()

        return PleasantHabit.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()
        return_serializer = PleasantHabitSerializer(new_habit)
        headers = self.get_success_headers(return_serializer.data)
        return Response(
            return_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class PleasantHabitsPublicListAPIView(ListAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.filter(is_public=True).order_by('id')
    permission_classes = [IsAuthenticated]
    pagination_class = PleasantHabitsPublicPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('user', 'is_public',)
    ordering_fields = ('id', 'action',)


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        new_payment = serializer.save()
        new_payment.user = self.request.user
        print(new_payment.connected_habit)
        if new_payment.connected_habit is not None and new_payment.reward is not None:
            raise ValidationError('Нельзя указать одновременно связанную привычку и вознаграждение')
        else:
            new_payment.save()


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('id')
    permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsAdminUser]


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('id')
    permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsAdminUser]
    pagination_class = HabitsPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('user', 'is_public',)
    ordering_fields = ('id', 'action',)

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.role == UserRoles.MODERATOR:
            return Habit.objects.all()

        return Habit.objects.filter(user=self.request.user)


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('id')
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
