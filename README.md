# Short-URL

A [Flask](https://flask.palletsprojects.com/en/1.1.x/) project which shortens any URL with randomised or user provided keywords.

# Quick Demo
![Demo](./images/Demo.gif "Demo")
## Setup

Ensure that the latest version of [Python](https://www.python.org/) is installed on your PC.

After installation, clone the repository and install the required dependencies by running the following commands one at a time:
    
    pip install -r requirements.txt

### Creating Database

To create the database run the following commands one at a time:

    $ python
    >>> from main import db
    >>> db.create_all()
    >>> exit()

### Run Development Server

And for the final step run the following:

    python main.py

### Public endpoint is at - http://127.0.0.1:5000
