from django.db import models

# Create your models here.

class TravelPlan(models.Model):
    destination = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    preferences = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    plan_details = models.TextField(blank=True)

    def __str__(self):
        return f"Travel Plan to {self.destination} ({self.start_date} to {self.end_date})"
