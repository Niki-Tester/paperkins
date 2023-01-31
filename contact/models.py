from django.db import models


class Contact(models.Model):
    class Meta:
        ordering = ["-date_time"]

    CHOICES = (
        ("general", "General Enquiry"),
        ("payment", "Payment Enquiry"),
        ("delivery", "Delivery Enquiry"),
        ("other", "Other"),
    )

    contact_name = models.CharField(max_length=256, null=False, blank=False)
    contact_email = models.EmailField(max_length=256, null=False, blank=False)

    query = models.CharField(
        choices=CHOICES, max_length=20, null=False, blank=False
    )

    message = models.TextField(max_length=1000, null=False, blank=False)
    date_time = models.DateTimeField(auto_now=True)
    response_sent = models.BooleanField(
        null=False, blank=False, default=False, editable=False
    )
    response_message = models.TextField(
        max_length=1000, null=False, blank=False, default=""
    )

    def __str__(self):
        return f"{self.query} | {self.date_time}"
