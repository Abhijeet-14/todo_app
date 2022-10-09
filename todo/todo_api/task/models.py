from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ("important", "Important Priority"),
        ("high", "High Priority"),
        ("medium", "Medium Priority"),
        ("low", "Low Priority"),
    ]

    task_id = models.BigAutoField(primary_key=True, auto_created=True, serialize=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    help = models.CharField(max_length=2)
    # prioirty = models.CharField(max_length=120, choices=PRIORITY_CHOICES, default="low")

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        return self.title[:30] + "..."
