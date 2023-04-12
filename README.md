# BJJQuestionnaire
BJJQuestionnaire app written in Django to show off routes, apps, authorization and some other things! :)


Django's official documentation was used throughout the creation of this demo app.


Steps to run BJJQuestionnaire  
1: Ensure you have both Python and pip installed. Development was done using Python 3.11.3  
2: Ensure you have git installed  
3: Clone down the app from this repo  
4: Install the most recent version of Django. Run `pip install django` in a terminal within the app  
5: Run using `python manage.py runserver`. This will allow the app to be accessed on http://127.0.0.1:8000/

BJJQuestionnaire uses Django's out of the box admin site to add and work with questions.  

Screenshots of the app can be seen below:  

![image](https://user-images.githubusercontent.com/35729390/231569704-86995488-6bab-4c0a-aa80-0423753ac1c6.png)  
The screen users are presented with when opening the app (with some beautiful UX design to compliment).  

![image](https://user-images.githubusercontent.com/35729390/231570094-d3ca1b5f-541e-4ed8-8a0b-844aec2409f7.png)  
On clicking into a question, the users will be directed onto the respective question, to enter their answer using radio buttons.  

![image](https://user-images.githubusercontent.com/35729390/231570287-a4ebcb6d-a8b8-4b6b-b1dd-97aa31344811.png)
After voting, the user can then see the number of votes for each answer in the questionnaire.  

![image](https://user-images.githubusercontent.com/35729390/231570523-bc70d6d7-e515-483d-9eaa-8223d2544076.png)  
Adding questions using the admin portal. A superuser must be created to access this part of the app.




