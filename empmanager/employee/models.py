from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Insurance(models.Model):
  name = models.CharField('保険名', max_length=20)
  created_at = models.DateTimeField('日付', default=timezone.now)

  def __str__(self):
      return self.name

class Therapist(models.Model):
  name = models.CharField('セラピスト名', max_length=20)
  created_at = models.DateTimeField('日付', default=timezone.now)

  def get_absolute_url(self):
    return reverse('therapist_detail', args=[str(self.id)])

  def __str__(self):
      return self.name



class Employee(models.Model):
    first_name = models.CharField('名', max_length=20)
    last_name = models.CharField('姓', max_length=20)
    insurance = models.ForeignKey(Insurance, verbose_name='保険名', on_delete=models.PROTECT, null=True, blank=True)
    therapist = models.ForeignKey(Therapist, verbose_name='セラピスト名', on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
      return '{0} {1}'.format(self.first_name, self.last_name)

    # def __str__(self):
    #     return self.name

    def save(self, *args, **kwargs):
        self.name = '{0} {1}'.format(self.first_name, self.last_name)
        super(Employee, self).save(*args, **kwargs)
