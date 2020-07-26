from django.db import models

# Create your models here.
MODE_CHOICES = (
    (-1, 'Translate'),
    (0, 'Tartil'),
    (1, 'Mojawad'),
    (2, 'Moalem'),
    (3, 'Tahdir'),
    (4, 'WORD'),
)

TYPE_CHOICES = (
    (-1, 'Deleted'),
    (1, 'Show'),
    (2, 'Translate'),
    (3, 'Tafsir'),
    (4, 'WORD'),
)


class ReciterType(models.Model):
    mode = models.IntegerField(null=True, blank=True, choices=MODE_CHOICES, default=0)


class Reciter(models.Model):
    r_id = models.IntegerField()
    r_img = models.CharField(max_length=500, verbose_name='تصویر')
    r_folder = models.CharField(max_length=500)
    r_nameAR = models.CharField(max_length=500)
    r_nameEN = models.CharField(max_length=500)
    r_nameFA = models.CharField(max_length=500)
    r_time = models.CharField(max_length=500, null=True, blank=True)
    r_url1 = models.CharField(max_length=500, null=False)
    r_size1 = models.IntegerField(null=False)
    r_quality1 = models.IntegerField(null=False)
    r_url2 = models.CharField(max_length=500, null=True, blank=True)
    r_size2 = models.IntegerField(null=True, blank=True)
    r_quality2 = models.IntegerField(null=True, blank=True)
    r_url3 = models.CharField(max_length=500, null=True, blank=True)
    r_size3 = models.IntegerField(null=True, blank=True)
    r_quality3 = models.IntegerField(null=True, blank=True)
    r_withBesm = models.IntegerField(null=True, blank=True)
    r_type = models.IntegerField(null=True, blank=True, choices=TYPE_CHOICES, default=1)
    r_ord = models.IntegerField(null=True, blank=True)
    r_mode = models.IntegerField(null=True, blank=True, choices=MODE_CHOICES, default=0)
    r_create = models.DateTimeField(editable=False, auto_now_add=True)
    r_update = models.DateTimeField(auto_now=True)
