from django.db import models

# Create your models here.
class Email(models.Model):
    sender_name = models.CharField(max_length=50)
    sender_email = models.EmailField()
    subject = models.CharField(max_length=127)
    message = models.TextField(max_length=255)
    origin = models.URLField()
    arrived_at = models.DateTimeField(auto_now=True)

    class  Meta:
        verbose_name_plural = "Arrived Emails "
        ordering = ["-arrived_at"]

