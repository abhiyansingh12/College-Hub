To run the code:
<!-- Navigates to the project folder where Django project is located. -->
1. cd /path/to/CollegeHUb-main

<!-- Activates the Virtual Environment -->
2. source venv/bin/activate

<!-- If made changes to the database models, apply migrations:
If no database changes were made, this step can be skipped. -->
3. python manage.py makemigrations
4. python manage.py migrate

<!-- Runs the Development Server -->
5. python manage.py runserver

<!-- Opens the browser  -->
6. http://127.0.0.1:****/

<!-- To access the admin panel: -->
7. http://127.0.0.1:****/admin/
<!-- Use the superuser credentials you created earlier to log in. -->

