# commentify
Modern Feedback Application
-----------------------------------------------------------------------------------------------------------------------------------------------
Hello, This Application-Commentify is created as part of Zoho Assesment as per the requirement.

Technology Stack:
Front end: HTML,CSS and Bootstrap (for Mobile first design model).
Backend: Python, Flask, SQLALCHEMY(ORM'S) is used on SQLITE Database.

This App is deployed on heroku cloud and is live, and the website url is given below:
You can instantly create a user in signup, and signin to the app to use it.

Site URL: https://commentify-zoho-assesment.herokuapp.com/

--------------------------------------------------------------------------------------------------------------------------------------------------
To run the app locally, Follow the below instructions. (Make sure python and pip are preinstalled in local)

1. Clone the repository to local.
2. Create a Virtual environment in the repo using the below command.
    "py -m venv venv"
3. Activate the Virtual Environment using the below command.
    "venv\scripts\activate"
4.All the needed packages are listed in requirements.txt file, Run the below command to install all the needed libraries in one command.
    "pip install -r requirements.txt"
5. After installing the libraries, Start the flask app using
    "flask run" command.
6. The flask app will be started and running in your designated local host.

-------------------------------------------------------------------------------------------------------------------------------------------------
All the modules mentioned have been completed.
This Application allows user to signup with email-id, password and a secret key.
Secret key is used to login, when the password is forgetten.
Once logged in, it takes you to the home page, where you can post comments and view other user's comments.
The filter module is implemented for displaying only the logged in user's comments, 
Additionally we can filter other users's comments too, and also reset the filters.

--------------------------------------------------------------------------------------------------------------------------------------------------
Hope all the needed essential details is documented above.

Looking forward for the feedback and result.
