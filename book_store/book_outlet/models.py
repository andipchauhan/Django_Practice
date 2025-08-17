from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title= models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)   # blank=True allows the field to be empty
    is_bestseller = models.BooleanField(default=False)      # if null=False(by default it is), you have to set a default value
    slug = models.SlugField(default="", null=False, db_index=True, unique=True) # Harry Potter 1 -> harry-potter-1
    # db_index=True creates an index on the slug field for faster lookups
    
    
    def save(self, *args, **kwargs):   # summary parameters
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)  # Call the "real" save() method.
    
    def __str__(self):
        return f"{self.title} ({self.rating})"
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})
        # return reverse("book_detail", args=[self.id])
    