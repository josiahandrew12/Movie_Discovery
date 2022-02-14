# Getting Started with my app
Step 1: Getting Started
To effectively run our application, we need to install python and pip.
Listed below are the necessary links.
Python
Link: https://www.python.org/downloads/
Pip
Link: https://pip.pypa.io/en/stable/cli/pip_install/

Step 2: SETTING UP VIRTUALENV
    1.	We need to set up the virtualenv. Which is a Python environment such that the Python interpreter, libraries, and scripts installed into it are isolated from those established in other virtual environments.cd to the main directory
    2.	type: “pip install virtualenv”
    3.	type: “source /flask/bin/activate” to active virtualenv

Step 3: IMPORT LIBRARIES
    1.	go to command line and
    2.	run: “pip install -r requirements.txt” in your shell to install all dependencies.

Step 4:
Now we are all set to run the application locally.
    1.	run: “flask run” in your shell to run the application locally.

    2.	Click http://127.0.0.1:5000/ (this may be different depending on the machine).
    3.	This will then re-direct you to the page below.


## Additional features

So, if I had more time, I would do a much better job with my CSS styling. I would have done the grid layout as the professor showed us in class. Then would have linked each random movie to its youtube trailer via their API

## Problems
So, the tmdb API was pretty straightforward, but the documentation was complicated for the wiki API. I had trouble with getting the right params and displaying the correct data. It would only display useless information I did not need. But once I did get the valid params, the link was a nested dictionary. But when I did figure it out out of 3 or 4 times or refreshing random movies, I would get 500 errors. And it was saying that there is no line for the None type. But eventually, I was able to figure it o

### Heroku Link
https://fathomless-shore-81275.herokuapp.com
