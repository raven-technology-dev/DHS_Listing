python3 manage.py makemigrations;
python3 manage.py migrate;
python3 manage.py collectstatic  --no-input;
echo ;
python3 manage.py runserver;
