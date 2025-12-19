from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    monthly_bill = models.FloatField()

    def risk_status(self):
        return "HIGH RISK" if self.monthly_bill > 1000 else "LOW RISK"

    def __str__(self):
        return self.name
