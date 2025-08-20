## DAY 1
```
1. python -m venv Django_Venv
2. Django_Venv\Scripts\activate
3. echo %VIRTUAL_ENV%
4. pip install django
5. cd Django_Venv
6. django-admin
<!-- python -m django --version -->
7. django-admin startproject monthly_challenges
8. cd monthly_challenges
9. dir
10. doskey /history
11. <!-- ..\..\Django_Venv\scripts\activate -->
12. python manage.py runserver
```

## DAY 2
```
1. ..\..\Django_Venv\scripts\activate
2. python manage.py startapp challenges 
```
#### DELETED THE Django_practice folder (now a repo in GitHub)
# URLs(routes) AND VIEWS
- views are the concrete python code(a function,class) that should be executed for different URLs(and HTTP methods)
- code that simply handles the incoming request, does something and returns a fitting response(HTML, JSON, etc)
### In Django_Venv
```
1. scripts/activate
2. django-admin startproject monthly_challenges
3. cd monthly_challenges
3. python manage.py startapp challenges
4. python manage.py runserver
```


### DAY 3
```
git config --global user.name "Andip Chauhan"
git config --global user.email "chauhan2244andip@gmail.com"
git init
git add monthly_challenges .gitignore COMMANDS.md
git commit -m "Initial commit with monthly_challenges"
git remote add origin https://github.com/andipchauhan/Django_Practice.git
git remote -v
git branch -m main
git pull origin main
git pull origin main --allow-unrelated-histories
git add README.md
git push -u origin main
```


### DAY 4
```
..\scripts\activate
git clone https://github.com/andipchauhan/Blog_Project_Django.git
django-admin startproject my_site
git remote -v
python manage.py startapp blog
python manage.py runserver
pip freeze > requirements.txt
git log
```

### DAY X - In Django_Practice
```
django-admin startproject book_store
python manage.py startapp book_outlet
```

# DAY X - Models and migrations
- add book_outet in INSTALLED_APPS in settings.py (Django will also auto pickup the MODELS in that app )
- Migrations define steps for Django to execute that will touch the DB and manipulate it e.g. creating new tables or updating existing ones
- Therefore, whenever we work with models, we need to **CREATE** migrations and also **RUN** those to actually tell Django to update DB
IN book_store (Overall project, NOT subapp)
```
python manage.py makemigrations  # Populates migration folders of all subApps/apps
python manage.py migrate            # Looks for all the migrations and runs them
```


### Interacting with DB through terminal pyhton shell
```
python manage.py shell
from book_outlet.models import Book

harry_potter = Book(title = "Harry Potter 1 - The Philosopher's Stone", rating=5)
harry_potter.save()  # will actually save data of this object in DB from this object

lord_of_the_rings = Book(title="Lord of the Rings", rating=4)
lord_of_the_rings.save()

Book.objects.all()
# modified __str__ in models.py to show actual object values
Book.objects.all()[1].title
```

### UPDATING and DELETING the data via python shell
```
python manage.py shell
from book_outlet.models import Book
harry_potter = Book.objects.all()[0]
harry_potter.title
lotr = Book.objects.all()[1]

harry_potter.author = "J.K. Rowling"
harry_potter.is_bestseller = True
harry_potter.save()             # updates the entry instead of creating a new one
Book.objects.all()[0].author

lotr.author = "J.R.R. Tolkien"
lotr.is_bestseller = True
lotr.save()
Book.objects.all()[1].author

# DELETING
harry_potter = Book.objects.all()[0]
harry_potter.delete()
Book.objects.all()[0]  # will show LOTR

Book.objects.all()[1].delete()
```

### CREATING ENTRIES instead of SAVE
```
Book.objects.create(title="Harry Potter 1", rating=5, author="J.K. Rowling", is_bestseller=True)
            # Book(title="1984", author="George Orwell").save()

Book.objects.create(title="My Life", rating=5, author="Andip Chauhan", is_bestseller=True)
Book.objects.create(title="Some Random Book", rating=3, author="Random dude", is_bestseller=False)
```


### QUERYING and FILTERING data
```
Book.objects.get(id=5)     # an id is forever gone and not reassigned when an object/entry is deleted
Book.objects.get(title="My Life")       # Only gets one entry
Book.objects.get(is_bestseller=True)    # Error - Because multiple matches


Book.objects.filter(is_bestseller=True)
Book.objects.filter(is_bestseller=True, rating=4)   # multiple filters

Book.objects.filter(rating__lte=4)    # lower than and equal (field lookups)
Book.objects.filter(rating__lte=4, title__icontains="Rings")    # case insensetive (in sqlite case insensetive by default)
```

### Quering with OR
```
from django.db.models import Q
Book.objects.filter(Q(rating__lt=4) | Q(is_bestseller=False))
Book.objects.filter(Q(rating__lt=4) | Q(is_bestseller=True) , Q(author="J.K. Rowling"))   
# can omit Q for and condition but it will have to come after all Q/OR conditions

```

### Chaining Queries
```
bestsellers = Book.objects.filter(is_bestseller=True)       # Not executed yet only stored in variable
amazing_bestsellers = Book.objects.filter(rating__gt=4)     # db still not touched
print(bestsellers)                                          # caches the result
print(amazing_bestsellers)                                  # will cache bestsellers and use for amazing_bestsellers quering as it is based on it
print(bestsellers)

# DB only hit once until now
# Wouldn't have cached if QUERYSET wasn't stored in a variable
```

### After slugify saving again to run custom save() function and populate slug column in existing entries
```
Book.objects.get(title="Harry Potter 1").slug
Book.objects.get(title="Harry Potter 1").save()
Book.objects.get(title="Harry Potter 1").slug

Book.objects.get(title__contains="some").save()
Book.objects.get(title="Some Random Book").save()

```



### Django Admin feature for DB
```
python manage.py createsuperuser
```

### DELETING ALL BOOKS
```
python manage.py makemigrations
python manage.py shell
from book_outlet.models import Book
Book.objects.all().delete()

python manage.py migrate
```

### Making new entries RELATIONSHIPS (MANY TO ONE RELATION)
```
python manage.py shell
from book_outlet.models import Book, Author
jk = Author(first_name="J.K.", last_name="Rowling")
jk.save()
Author.objects.all()

hp1= Book(title="Harry Potter 1", rating=5, is_bestseller=True, slug="harry-potter-1", author=jk)
harrypotter = Book.objects.get(title="Harry Potter 1")
harrypotter.author.first_name
harrypotter.author.last_name

books_by_rowling = Book.objects.filter(author__last_name__contains="ling")
books_by_rowling
books_by_rowling[0].title


jkr = Author.objects.get(first_name="J.K.")
jkr
jkr.book_set
jkr.book_set.all()
```

- Set "related_name='books'" in models

```
python manage.py makemigrations
python manage.py migrate
python manage.py shell
from book_outlet.models import Book, Author
jkr = Author.objects.get(first_name="J.K.")
jkr.books
jkr.books.all()
jkr.books.filter(title__contains="arr")
jkr.books.filter(rating__gt=3)
```

### ONE TO ONE RELATIONSHIP
```
python manage.py shell
from book_outlet.models import Book, Author, Address
add1 = Address(street="Some street", postal_code="12345", city="New York")
add1.save()
add2 = Address(street="Other street", postal_code="54321", city="London")
add2.save()

jkr = Author.objects.get(first_name="J.K.")
jkr.address = add1
jkr.save()
jkr.address
jkr.address.city

Address.objects.all()[0].author
Address.objects.all()[0].author.first_name
```

### MANY TO MANY RELATIONSHIP  (add() methods exists for many to many)
```
python manage.py shell
from book_outlet.models import Book, Country
hp1 = Book.objects.all()[0]
hp1.published_countries.all()

India = Country(name="India", code="+91")
India.save()
hp1.published_countries.add(India)
hp1.published_countries.filter(code__contains=91)

ind = Country.objects.all()[0]
ind.book_set.all()
in.books.all()                    # after setting related_name in models and migrating
```



# FORMS
```
django-admin startproject feedback
cd feedback
python manage.py startapp reviews
python manage.py shell
from reviews.models import Review
Review.objects.all()
Review.objects.all()[0].review_text
```