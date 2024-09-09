echo "BUILD START"
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
python manage.py makemigrations --noinput --clear
python manage.py migrate --noinput --clear
echo "BUILD END"