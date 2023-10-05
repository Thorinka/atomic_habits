from django.urls import path

from habits.apps import HabitsConfig
from rest_framework.routers import DefaultRouter

from habits.views import PleasantHabitViewSet, HabitCreateAPIView, HabitListAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, PublicHabitsListView

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'pleasant_habits', PleasantHabitViewSet, basename='pleasant_habits')


urlpatterns = [
    path('habits/create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('habits/view/', HabitListAPIView.as_view(), name='habits_list'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habits/destroy/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_destroy'),

    path('habits/public/view/', PublicHabitsListView.as_view(), name='public_habits_list'),
] + router.urls
