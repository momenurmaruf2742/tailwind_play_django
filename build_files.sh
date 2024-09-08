echo "BUILD START"
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
echo "BUILD END"