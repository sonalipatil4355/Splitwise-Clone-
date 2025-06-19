"# Splitwise-Clone-" 
Create groups and assign users
Add expenses to a group
View balances — who owes whom
Simple, responsive UI using Django templates

. Clone & Activate
py -m venv env
cd env/acripts
activated
. Install Dependencies
pip install -r requirements.txt
. Apply Migrations
python manage.py migrate
. Run the Server
python manage.py runserver

URLs=>

URL	Description
/groups/-List of groups
/groups/create/-Create new group
/expenses/add/-Add expense
/groups/<id>/balances/-View balances per group


-Technologies Used
Django & Django REST Framework
SQLite (Dev DB)
TailwindCSS
HTML templates (no React)