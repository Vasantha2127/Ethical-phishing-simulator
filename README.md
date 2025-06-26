# Ethical-phishing-simulator

# Ethical Phishing Simulation Platform

This is an internship project to simulate phishing campaigns for **training and educational** purposes using Flask, SQLite, and basic HTML/CSS. It helps security teams or trainers to test how users react to phishing emails in a safe lab environment.

---

## Tech Stack

1. **Create phishing campaigns** by entering email and custom message.
2. **Generate phishing simulation links** for safe testing.
3. **Track clicks** and timestamps for simulated phishing emails.
4. **Analytics Dashboard** showing user interactions.
5. **Awareness Page** educating users once they click the phishing link.
---

## Key Features

- Create phishing email templates (custom content)
- Generate simulation links
- Log email clicks (email + timestamp)
- Display analytics dashboard (click count per template)
- Educate users after clicking (simulation landing page)

---

## How I Built It (Step-by-Step)

### Step 1: Created Project Folder
Created a folder named `phishing-sim` with the following structure:
phishing-sim/
├── app.py # Main Flask app
├── models.py # Creates and initializes SQLite database
├── requirements.txt # Python packages used
├── database.db # Auto-generated SQLite DB file
├── templates/
│ ├── index.html # Main UI for creating phishing campaigns
│ ├── clicked.html # Displayed when a user clicks the phishing link
│ └── analytics.html # View analytics of who clicked and when

### Step 2: Set Up the Project Environment
- Installed Python 3.x and Flask using:

  pip install flask
Created project folder: phishing-sim

Made app.py for main Flask app

Created models.py to set up the database

Install Required Packages
Make sure Python is installed. Then run:

pip install -r requirements.txt

### Step 3: Created the Database
In models.py, I wrote SQL to create:

templates table – stores phishing templates

logs table – stores click logs

Ran it using:

python models.py
This created database.db

### Step 4: Designed Flask App (app.py)
Added features:

/ → Home page to add/view templates

/create → Store new phishing templates

/send/<id> → Generate simulation links

/clicked/<id> → Log when someone clicks the link

/analytics → Show click counts by template

### Step 5: Built HTML Templates
index.html: Contains a form to create templates and lists all saved ones.

analytics.html: Table displaying how many users clicked on which template.

Used Flask's render_template to dynamically render HTML.

Step 5: Ran and Tested the Application
Started app:
python app.py

Opened browser at:
http://localhost:5000

Tested:
Created phishing templates

Generated simulation links (e.g. /clicked/1?email=test@lab.com)

Clicked link to simulate user response

Viewed analytics dashboard showing click logs

