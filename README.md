# celeryexample2

http://www.reddit.com/r/django/comments/34rzko/newbie_question_about_proper_way_to_use_celery/cqxudoc

```
git clone https://github.com/dj-jar/celeryexample2.git
cd celeryexample2/
pip install -r pip-requirements.txt
python manage.py makemigrations
python manage.py migrate
celery -A problemproject worker -l info &
python manage.py runserver
```
