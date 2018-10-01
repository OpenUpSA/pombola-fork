from django.db import models


class Message(models.Model):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDING
    )
    text = models.TextField()
    msisdn = models.TextField()
    datetime = models.DateTimeField()

    class Meta:
        unique_together = ('text', 'msisdn', 'datetime')
        ordering = ['-datetime']
