# django-workshop
### Install Django
[Download python](https://www.python.org/downloads/)
and follow installing statements
### Install Django
pip install django
### Get Start with Django
1. django admin startproject project-name
   1. (note) dont name your project test or django
2. cd project folder
3. python manage.py startapp  app-name
4. cd project folder
5. open setting.py
7. add the new app in INSTALLED_APPS
   1. dont messing , at the and of list
8. open urls.py
9. import include from django.conf.urls
10. add ligne in urlpatterns
   1. url(r'^', include('app-name.urls'),

