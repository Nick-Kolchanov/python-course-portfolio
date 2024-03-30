from django.test import TestCase
from jobs.models import Job


class JobTestCase(TestCase):
    """
    Тестирование функций
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.
        :return:
        """

        Job.objects.create(
            image="Путь к картинке",
            description="Описание работы 1",
            detailed_description="Описание работы 1 со всеми деталями" * 50,
        )

    def test_job_messages_creation(self) -> None:
        """
        Тестирование модели работ.
        :return:
        """

        job = Job.objects.get(description="Описание работы 1")

        detailed_description = "Описание работы 1 со всеми деталями" * 50
        self.assertEqual(job.summary(), detailed_description[:80] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')
