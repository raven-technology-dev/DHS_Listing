source .venv/bin/activate;
git pull git@github.com:buzz-buzz-Alaska/dhs_listing.git;
pip install --upgrade -r requirements.txt;
sudo apt update && sudo apt dist-upgrade;
python3 manage.py makemigrations;
python3 manage.py migrate;
python3 manage.py collectstatic --no-input;
sudo systemctl restart gunicorn;
