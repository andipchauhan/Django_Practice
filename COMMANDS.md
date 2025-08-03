## DAY 1
```
1. python -m venv Django_Venv
2. Django_Venv\Scripts\activate
3. echo %VIRTUAL_ENV%
4. pip install django
5. cd Django_Venv
6. django-admin
<!-- python -m django --version -->
7. django-admin startproject Django_Practice
8. cd Django_Practice
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
git add remote add origin https://github.com/andipchauhan/Django_Practice.git
git remote -v
git branch -m main
git pull origin main
git pull origin main --allow-unrelated-histories
git add README.md
git push -u origin main
```
