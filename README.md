# django-workshop
### Install python
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
6. add the new app in INSTALLED_APPS
   1. don't forget , at the end of list
7. open urls.py
8. import include from django.conf.urls
9. add ligne in urlpatterns
   1. url(r'^', include('app-name.urls'),
10. cd ..
11. cd app folder
12. create new file name urls.py
13. add the following code to urls.py

```python
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        ]
```

14. save change
15. open views.py
16. import HttpResponse from django.http
17. add this function

```python
def index(request):
    return HttpResponse('hello')
```

after try

```python
def index(request):
    return HttpResponse('<h1>hello</h1>')
```
18. cd ..
19. python manage.py runserver
20. open browser link 127.0.0.1:8000
### Result
![Alt text](/image/image1.png)

