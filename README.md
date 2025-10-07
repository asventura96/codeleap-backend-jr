# CodeLeap Backend Challenge

This is the backend for the CodeLeap engineering test, built with Django and Django REST Framework.

## How to Run the Project

1. **Clone the repository:**

    ```bash
    git clone https://github.com/asventura96/codeleap-backend-jr.git
    cd codeleap-backend-jr
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Copy the example `.env.example` file to a new file named `.env`.

    ```bash
    # On Windows
    copy .env.example .env
    # On macOS/Linux
    cp .env.example .env
    ```

    *Open the `.env` file and change the values if necessary. For this project, the default values are sufficient.*

5. **Apply the database migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser to test the API:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the server:**

    ```bash
    python manage.py runserver
    ```

---

## Author

Developed by **André Ventura**.

- **Portfolio:** [asventura.me](https://asventura.me)
- **LinkedIn:** [André Ventura](https://www.linkedin.com/in/asventura96)
- **GitHub:** [asventura96](https://github.com/asventura96)
