from django.contrib import admin
from .models import Insurance, Employee, Therapist

# Register your models here.
admin.site.register(Insurance)
admin.site.register(Employee)
admin.site.register(Therapist)
