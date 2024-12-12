# Quiz Application - Django Project

This is a simple Django-based Quiz Application. Follow the steps below to set up and run the project.

## Steps to Run the Application

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/narerndra369/QuizApplication.git
```

### 2. Create a Virtual Environment

Navigate to the project directory:

```bash
cd QuizApplication
```

Create a virtual environment named `myenv`:

```bash
python -m venv myenv
```

### 2.1 Activate the Virtual Environment

- **On Windows:**

```bash
myenv\Scripts\activate
```

- **On MacOS/Linux:**

```bash
source myenv/bin/activate
```

### 3. Install Django

With the virtual environment activated, install Django:

```bash
pip install django
```

### 4. Make Migrations

Run migrations to set up the database:

```bash
python manage.py migrate
```

### 5. Run the Application

Finally, start the Django development server:

```bash
python manage.py runserver
```

The application should now be running at `http://127.0.0.1:8000/`.
