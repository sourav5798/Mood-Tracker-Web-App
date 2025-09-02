from django.db import models
from django.utils import timezone

MOOD_CHOICES = [
    ('Happy', 'Happy'),
    ('Sad', 'Sad'),
    ('Angry', 'Angry'),
    ('Relaxed', 'Relaxed'),
    ('Excited', 'Excited'),
]

class MoodEntry(models.Model):
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    note = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.date} - {self.mood}"
