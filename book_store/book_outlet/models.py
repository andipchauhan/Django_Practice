from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True) 
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}"

    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, )   # One-to-one relationship with Address
    # no need for related_name here as it is same and not author_set like in foreign key
    # becuase there will not be a set of authors for an address, like set of books for an author
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title= models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books') # Many-to-one relationship with Author
    is_bestseller = models.BooleanField(default=False)      
    slug = models.SlugField(default="", null=False, db_index=True, unique=True) # Harry Potter 1 -> harry-potter-1
    published_countries = models.ManyToManyField(Country, related_name="books")  # Many-to-many relationship with Country
    # cannot add on_delete here as it is not a foreign key, but a many-to-many field
    # becuase behind the scenes it creates a new table to store each entry between Book and Country

    def __str__(self):
        return f"{self.title} ({self.rating} stars)"
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})
        # return reverse("book_detail", args=[self.id])
    
    # def save(self, *args, **kwargs):   # summary parameters
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)  # Call the "real" save() method.
    # Prepopulated fields in admin interface does this automatically, so no need to override save method