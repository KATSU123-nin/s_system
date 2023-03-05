from django.db import models
from django.utils import timezone

from employee.models import Employee


class Pain(models.Model):
    name = models.CharField('痛みの具合', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name


class Range(models.Model):
    name = models.CharField('可動域制限', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name


class RehaPlan(models.Model):
    name = models.CharField('リハビリの内容', max_length=40)
    created_at = models.DateTimeField('日付', default=timezone.now)
    # models.ManyToManyFieldにて対応する

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField('コメント', max_length=400)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name


class KarteInfo(models.Model):
    patient = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name='患者名')
    therapist = models.ForeignKey(Employee, 
        on_delete=models.deletion.CASCADE,
        related_name="related_therapist",
        verbose_name="担当セラピスト",
    ),
    reha_at = models.DateField('リハビリ実施日', default=timezone.now)
    pain = models.ForeignKey(
        Pain,  on_delete=models.CASCADE, verbose_name='痛みの具合', blank=True)
    range = models.ForeignKey(
        Range,  on_delete=models.CASCADE, verbose_name='可動域制限', blank=True)
    rehaplan = models.ManyToManyField(
        RehaPlan, verbose_name='リハ内容', blank=True)
    comment = models.CharField('コメント', max_length=400)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return str(self.patient)
