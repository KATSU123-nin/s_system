from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    therapist_name = models.CharField(max_length=100)
    insurance = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    onset_date = models.DateField()
    reha_start = models.DateField()
    karte_id = models.CharField(max_length=100)
    birth_date = models.DateField()
    sex = models.CharField(max_length=10)
    short_term_goal = models.TextField()
    long_term_goal = models.TextField()
    treatment_policy = models.TextField()
    treatment_content = models.TextField()

    def __str__(self):
        return self.name

