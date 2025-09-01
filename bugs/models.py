from django.db import models

class Bug(models.Model):
    STATUS_CHOICES = [("open","Ouvert"),("closed","Fermé")]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="open")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.status}] {self.title}"
