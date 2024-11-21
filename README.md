# Wedding Manager 💍

A system developed in **Django** to manage wedding guests and gift lists, making it easy and organized for the bride and groom!

---

## 🚀 Features

- **Guest Management**:
  - Register guests with their contact details and confirmation status.

- **Gift List**:
  - Create a personalized gift list with prices and importance levels.
  - Allow guests to reserve gifts for the couple.

---

## 🛠️ Technologies Used

- **Back-end**: Django 
- **Database**: SQLite 
- **Frontend**: HTML5, CSS3, Tailwind CSS
- **Other Tools**: Python, Git

---

## ⚙️ How to Set Up and Run the Project

1.  Clone the repository:
   
    `git clone https://github.com/ricardotemporal/wedding-manager.git`
    `cd wedding-manager`

2.  Create and activate a virtual environment:

    - `python -m venv env`
    - `source env/bin/activate`  # Linux/Mac
    - `env\Scripts\activate`    # Windows

3.  Install the dependencies:

    `pip install -r requirements.txt`

3.  Apply the database migrations:

    `python manage.py makemigrations`
    `python manage.py migrate`

4.  Start the development server:

    `python manage.py runserver`

Access the system at http://127.0.0.1:8000/
