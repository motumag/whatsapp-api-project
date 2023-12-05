Steps to run the project
For DB users:
user admin: admin
password: admin123
1. git clone https://github.com/motumag/whatsapp-api-project.git
2. cd WhatsApp folder and run the bellow command
3. python -m venv venv =>to create a vertual environment 
4. venv\Script\activate => to activate the virtual environment 
5. pip install -r requirements.txt =>This will install all required libraries 
6. npm install -g wscat =>globally for websocket
7. python manage.py createsupperuser => to create a supper user
8. python manage.py makemigrations =>make migration to database
9. python manage.py migrate => Migrate to DB
10. python manage.py runserver => to run the application
11. http://localhost:8000/swagger/ => to get swagger documentation