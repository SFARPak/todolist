import random
from django.db import models
from django.utils.text import slugify

class List(models.Model):
    
    STATUS_CHOICES = (
    ("backlog", "Backlog"),
    ("inprogress", "In Progress"),
    ("done", "Done"),
    )

    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    slug = models.SlugField(max_length=230, blank=True)
    
    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug = slugify(self.first_name)
    #     super().save(*args, **kwargs)

    def __str__ (self):
        return f'{self.title} {self.title}' 

    def get_absolute_url(self):
         return f"/todo/{self.slug}"

    def get_edit_url(self):
        return f"/todo/{self.slug}/edit"
    
    def get_delete_url(self):
        return f"/todo/{self.slug}/delete"