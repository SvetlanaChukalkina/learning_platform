from django.core.management.base import BaseCommand

from users.models import Payment, User


class Command(BaseCommand):
    """Команда для добавления тестовых данных о платежах"""

    def handle(self, *args, **kwargs):
        user, _ = User.objects.get_or_create(email="testtesttest@yandex.ru")

        payments = [
            {
                "user": user,
                "date": "2025-01-01",
                "payment_for_course": 1,
                "total_payment": 5000,
                "type": "перевод",
            },
            {
                "user": user,
                "date": "2025-05-05",
                "payment_for_lesson": 1,
                "total_payment": 1000,
                "type": "наличные",
            },
        ]

        for payment in payments:
            payment, created = Payment.objects.get_or_create(**payments)
            if created:
                self.stdout.write(self.style.SUCCESS("Successfully added payment"))
            else:
                self.stdout.write(self.style.WARNING("Payment already exists"))
