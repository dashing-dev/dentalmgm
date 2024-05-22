from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=100)
    address = models.TextField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    problem_description = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    installments_done = models.DecimalField(max_digits=10, decimal_places=2)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    app_date = models.DateTimeField(null=True)
    
    
    def __str__(self):
        return self.name