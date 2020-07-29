# Developer Portfolio 🚀

## A beautiful portfolio web app wirtten in ***Python3*** using ***Django3.0*** web framework for developers :neckbeard:


![jawed](https://user-images.githubusercontent.com/12079219/88625754-0473f900-d0c7-11ea-94b6-aed7882ba93d.gif)

## Sections

⦿ 🏠 Home 

⦿ 👤 About

⦿ 🛠 Skills

⦿ 📋 Resume

⦿ 📨 Contact

***To view a live example, visit - [demo](https://j4w3d.github.io/)***

## Setup ⚙️

Before going to setup this app You will need to install [python3](https://www.python.org/downloads/source/) & web framework [django3](https://docs.djangoproject.com/en/3.0/intro/install/) on your machine.

```
python3.7 or above
django3.0 or above
```

**Install `git` and clone this repo

```
# Clone this repository
git clone https://github.com/j4w3d/devfolio.git

# Enter into cloned repo
cd devfolio

# Create a virtual environment for your app
python3 -m venv venv


# Activate the virtual environment
source venv/bin/activate

# Upgrade pip & Install dependencies using pip
pip install --upgrade pip
pip install -r requirements.txt

# Collect staticfiles
python manage.py collectstatic

# Run the app
python manage.py runserver
```

By default this app will run on http://127.0.0.1:8000/


## To customize the data of portfolio app sections as per your requirements you need to edit - `resume/settings.py` file

```
# Edit: resume/settings.py

# Edit this file to display your details on portfolio page

DEVFOLIO_SETTINGS = {

    # Section - Home
    "HOME" : {
        # Customize your title & subtitle on landing page
        "title": "Jawed Salim",
        "subtitles": [
            "DevOps Engineer",
            "Python Developer",
            "Technophile"
        ]
    },

    # Section - About
    "ABOUT" : {

        # Title & your roles/skills list
        "title": "DevOps Engineer | Backend Developer ",
        "roles": [
            # List of roles/tasks - What you do
            
            "⚡ Maintain GIT repositories for DevOps environment: automation code and configuration.",

            "⚡ Write RESTful APIs in Python with variuos Webframeworks like: Flask, FastApi & Django.",
        ]
    },

    # Section - Skills
    "SKILLS" : { ..... },

    # Section - Skills
    #               - Proficiency
    "PROFICIENCY" : { ..... },

    # Section - RESUME
    "RESUME" : { ..... },

    # Section - contact
    "CONTACT" : { ..... },
    
    # Social Media links
    "SOCIAL" : {
        "title" : "Want to get connected or just say Hello? Follow me on the social channels below.",
        "sites" : [
            {
                "name" : "linkedin",
                "link" : "https://www.linkedin.com/in/j4w3d/"
            },
            {
                "name" : "github",
                "link" : "https://github.com/j4w3d/"
            },
            {
                "name" : "twitter",
                "link" : "https://twitter.com/jawedsalim10"
            },
            {
                "name" : "skype",
                "link" : "https://join.skype.com/invite/UiQ03EiXED9p"
            },

            # NOTE: you can use instagram & facebook too.
        ]
    }

}


```


## TODO List:
Anyone who can make it better or can help us with these is most welcomed to open a [pull request](https://github.com/j4w3d/devfolio/pulls).
- Add  more sections like Achievments/Awards, Services, Blogs etc.
- Enable dark theme
- Add multiple themes & so on.

