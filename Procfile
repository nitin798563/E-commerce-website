web: bash -c "python manage.py makemigrations && 
python manage.py migrate && 
gunicorn Ecommerce.wsgi:application --bind 0.0.0.0:$PORT"
