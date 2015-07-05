emacs requirements.txt
mkdir first_light
virtualenv ./first_light/
(virtualenv --python=/usr/bin/python3 venv)
(virtualenb -p python3 venv)
source ./first_light/bin/activate
pip install -U -r requirements.txt
deactivate

REOPEN INSTALLED SOURCE
source ./first_light/bin/activate

SAVE REQUIREMENTS
pip freeze > requirements.txt
