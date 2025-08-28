## Django Practice and Notes

when we extend a template in django, the extended template gets the context of parent template

template for html templates
static for css, images, files, etc


Django is a framework and not a web server, runserver command runs a development only server not optimcal for production

wsgi and asgi will work as entrypoints for incomign requests

Django doesn't serve static files automatically(CSS, user uploads), hence we need to configure the static setting in global URLs

sqlite3 alternatives for larger websites with heavier traffic