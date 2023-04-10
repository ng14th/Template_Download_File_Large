from django.db import models

# Create your models here.
class FileTemplate(models.Model):
    header_1 = models.CharField(max_length=255)
    header_2 = models.CharField(max_length=255)
    header_3 = models.CharField(max_length=255)
    header_4 = models.CharField(max_length=255)
    header_5 = models.CharField(max_length=255)
    header_6 = models.CharField(max_length=255)
    header_7 = models.CharField(max_length=255)
    header_8 = models.CharField(max_length=255)
    header_9 = models.CharField(max_length=255)
    header_10 = models.CharField(max_length=255)
    header_11 = models.CharField(max_length=255)
    header_12 = models.CharField(max_length=255)
    header_13 = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = "file_templates"
