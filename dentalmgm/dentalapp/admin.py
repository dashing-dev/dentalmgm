from django.contrib import admin

# Register your models here.
from .models import Doctor  # Import your model(s)
from .models import Patient

admin.site.register(Doctor)
admin.site.register(Patient)