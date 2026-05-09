from django.db import models


class Lead(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("negotiation", "Negotiation"),
        ("won", "Won"),
        ("lost", "Lost"),
    ]

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    company = models.CharField(max_length=150)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"