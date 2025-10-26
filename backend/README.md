## Backend

**Tech:** Django REST Framework  

**Features:**
- API endpoint: `/api/posts/` returning paginated posts
- Admin panel to manage posts: `/admin/`

**Setup:**
```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Load sample posts
python manage.py loaddata posts/fixtures/sample_posts.json

# Create superuser (optional for admin)
python manage.py createsuperuser

# Run server
python manage.py runserver
