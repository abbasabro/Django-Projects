# Django-Projects

Welcome to my `Django-Projects` repository! This repository serves as a collection of various Django applications I'm building to enhance my skills and explore different aspects of the Django framework, particularly focusing on the Object-Relational Mapper (ORM).

As I continue my learning journey, I'll be adding more diverse projects to this repository. Feel free to explore, provide feedback, or even contribute!

---

## 📊 Expense Tracker

The "Expense Tracker" is the first project showcased in this repository. It's a simple yet effective web application designed to help users manage their personal finances by tracking income and expenses.

My primary goal with this project was to gain a deeper understanding and practical experience with **Django's ORM (Object-Relational Mapper)**. I focused on designing models, performing database queries, filtering data, and using aggregation functions to calculate financial summaries.

### ✨ Features

The Expense Tracker provides the following functionalities:

* **Add Transactions:** Easily input new financial transactions with a description and an amount. Positive amounts are treated as income, while negative amounts are expenses.
* **Real-time Balance:** Instantly view your current overall balance, which is dynamically updated with each transaction.
* **Income/Expense Summary:** See a clear breakdown of your total income and total expenses.
* **Transaction History:** A chronological list of all your recorded transactions, making it easy to review past financial activities.
* **Delete Transactions:** Remove individual transactions from your history as needed.
* **User-Friendly Interface:** The UI is designed to be clean and intuitive, making expense tracking straightforward.

### 🛠️ Technologies Used

* **Backend:** Django (Python Web Framework)
* **Database:** PostgreSQL (using `psycopg2` for connectivity)
* **Frontend (HTML/CSS/JS):** HTML templating, CSS for styling, and basic JavaScript for alert messages.
    * *UI Inspiration:* The styling for this project was heavily inspired by a great design found on CodePen: [https://codepen.io/solygambas/pen/OJbqyro](CodePenUI)

### 🚀 Getting Started

To run this project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/abbasabro/Django-Projects.git]
    cd Django-Projects/expense
    ```
 

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies:**
    *(You'll need to create a `requirements.txt` file inside the `expense-tracker` project folder first)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up PostgreSQL database:**
    Ensure you have PostgreSQL installed and running. Create a database named `expense` and a user `postgres` with password `admin` (matching the `DATABASES` settings). You might need to adjust these credentials in `expense-tracker/expense/settings.py` for your local setup or, ideally, use environment variables for security.

5.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

### 🛣️ Future Plans

This is just the beginning! I plan to expand this repository with more Django projects covering various topics such as:

* User authentication and authorization
* API development (REST APIs with Django Rest Framework)
* Integration with external services
* More complex data models and relationships
* Testing strategies
* Deployment practices

Stay tuned for updates!

---

### Author

[Abbas Abro]
* GitHub: [https://github.com/abbasabro]
* LinkedIn: [https://www.linkedin.com/in/abro-abbas/?originalSubdomain=pk]
