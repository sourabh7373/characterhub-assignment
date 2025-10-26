Backend Django app.
Run:
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata posts/fixtures/sample_posts.json
python manage.py runserver
