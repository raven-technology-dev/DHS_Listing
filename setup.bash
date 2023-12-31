python3 -m venv .venv;
source .venv/bin/activate;
pip install --upgrade -r requirements.txt;
sudo apt install --upgrade libpq-dev postgresql postgresql-contrib;
mkdir media;
mkdir static;
mkdir logging;
echo "" >> logging/debug.log;
