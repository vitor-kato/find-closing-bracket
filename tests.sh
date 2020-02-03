echo "Running tests..."

echo "Testing backend api..."
cd backend
pipenv run python manage.py test api

echo "Testing libs..."
cd libs
python -m unittest
