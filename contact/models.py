from django.db import models


class Contact(models.Model):

    CHOICES = (
        ('general', 'General Enquiry'),
        ('payment', 'Payment Enquiry'),
        ('delivery', 'Delivery Enquiry'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=256, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)

    query = models.CharField(
        choices=CHOICES, max_length=20, null=False, blank=False)

    message = models.TextField(max_length=250, null=False, blank=False)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.query} | {self.date_time}'
