# Post_Management_API

### Description
In this assignment, the objective is to develop a Django project titled "Post Management API" aimed at establishing a robust API infrastructure for efficient post management. The primary focus is on the creation of two essential API endpoints: a POST API for generating new posts and a GET API for retrieving a list of existing posts.

## Installation
* After Cloning the github repository follow to below steps.


* If you wish to run your own build, first ensure you have python version **3.10.5** globally installed in your computer.
* After that, run another command in the command prompt to check if the Django web framework version **4.2.5** is installed or not:

  
          $ django-admin --version

* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

        $ pip install virtualenv

* Then, to activate it, run:


         $  source./django env/bin/activate

  
* In your terminal navigate to an empty folder and install Django REST framework:


            $  pip install django_rest_framework

  
* Now for creating a new django app run this command:


          $ django-admin startproject app
  
* Install the dependencies needed to run the app:

  
         $ pip install -r requirements.txt

* Install PyYAML :

        $pip install pyyaml

* Install uritemplate:

        $ pip install uritemplate
  

* Install Django Swagger module:

      $ pip install django-rest-swagger
    

* Make those migrations work:
  
        $ python manage.py migrate`

* Run the server using command:
  
        $ python manage.py runserver

* You can now access the file api service on your browser by using

        $ http://localhost:8000/api/posts/

* The schema will now be found at:

        $ http://http//127.0.0.1:8000/api_schema

* API docs will now be found at:
        $ http://127.0.0.1:8000/docs/
