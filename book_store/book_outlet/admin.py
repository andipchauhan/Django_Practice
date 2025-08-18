from django.contrib import admin
from .models import Book, Author, Address, Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)  # Makes the slug field read-only in the admin interface
    prepopulated_fields={"slug": ('title',)}  # Automatically populates the slug field based on the field in tuple (title field here)
    list_filter = ("author", "rating",)  # Adds filters in the admin interface
    list_display = ("title", "author", "rating")  # Fields to display in the list view of the admin interface  


class AuthorAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Book, BookAdmin)  # This registers the Book model with the Django admin site
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, )
admin.site.register(Country, )