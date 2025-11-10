from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from fitness.models import Programs, Exercises
from django.contrib.auth import get_user_model
User = get_user_model()


class FitnessViewsTests(TestCase):

    def setUp(self):
        self.client = Client()

        # Створюємо тестові об’єкти
        self.program1 = Programs.objects.create(
            name="Beginner Strength Plan",
            slug="beginner-strength",
            description="Basic weight training program",
            difficulty="beginner",
            duration="short",
            goal="strength"
        )

        self.program2 = Programs.objects.create(
            name="Advanced Weight Loss",
            slug="advanced-weight-loss",
            description="High intensity fat burn program",
            difficulty="advanced",
            duration="long",
            goal="weight_loss"
        )

        self.exercise = Exercises.objects.create(
            name="Push-ups",
            slug="push-ups",
            content="Push-ups description",
            repetitions=10,
            times=3
        )

        self.program1.exercises.add(self.exercise)

    def test_home_view_status(self):
        """Перевірка доступності головної сторінки"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fitness/home.html')

    def test_programs_home_view(self):
        """Перевірка відображення списку програм"""
        response = self.client.get(reverse('programs_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Beginner Strength Plan")

    def test_search_query_finds_program(self):
        response = self.client.get(reverse('programs_home'), {'q': 'Advanced'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Advanced Weight Loss")

    def test_filter_by_goal(self):
        """Фільтрація за ціллю"""
        response = self.client.get(reverse('programs_home'), {'goal': 'strength'})
        self.assertContains(response, "Beginner Strength Plan")
        self.assertNotContains(response, "Advanced Weight Loss")

    def test_skyline_applied(self):
        """Skyline повинен відфільтрувати гірші варіанти"""
        response = self.client.get(reverse('programs_home'), {'q': 'weight'})
        self.assertEqual(response.status_code, 200)
        self.assertIn("programs", response.context)
        # Переконуємось, що не повернуто пустий queryset
        self.assertTrue(response.context['programs'].exists())

    def test_program_detail_view(self):
        """Детальна сторінка програми"""
        response = self.client.get(reverse('program', args=[self.program1.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Beginner Strength Plan")

    def test_exercise_detail_view(self):
        """Перевірка сторінки вправи"""
        response = self.client.get(reverse('exercise', args=[self.exercise.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Push-ups")

    def test_protected_post_requires_login(self):
        """POST-запит до Program (вибір програми) вимагає авторизації"""
        response = self.client.post(reverse('program', args=[self.program1.slug]))
        self.assertEqual(response.status_code, 302)  # Перенаправлення на логін

        user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('program', args=[self.program1.slug]))
        self.assertEqual(response.status_code, 302)  # Перенаправлення до профілю

