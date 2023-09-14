
set -o errexit #This command sets the option errexit or e, which means that the script will exit immediately if any command returns a non-zero exit status (i.e., encounters an error). This ensures that if any of the subsequent commands fail, the script will stop executing further.

source /home/power-gym.com.ar/public_html/bin/activate

git pull

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py makemigrations

python manage.py migrate
