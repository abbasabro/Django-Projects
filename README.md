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

---

## 🖼️ Image Resizer

The "Image Resizer" is a utility project demonstrating automated image processing within a Django application. It leverages Django Signals and the Pillow library to create different-sized thumbnails whenever an original image is uploaded.

This project was built to explore:

* **Django Signals:** How to use `post_save` signals to trigger actions after an object is saved to the database.
* **Image Processing:** Integrating `Pillow` (PIL Fork) for resizing and manipulating images.
* **File Management:** Handling image uploads and saving derived files within Django's media system.

### ✨ Features

The Image Resizer offers the following core functionalities:

* **Image Upload:** Users can upload original images through the Django admin interface (or a custom form, if built).
* **Automated Thumbnail Generation:** Upon successful upload of an original image, the system automatically generates three different sizes of thumbnails:
    * **Small:** 100x100 pixels
    * **Medium:** 300x300 pixels
    * **Large:** 700x700 pixels
* **Thumbnail Storage:** The generated thumbnails are saved to a designated media directory, linked to the original image record in the database.
* **Efficient Processing:** Uses `PIL.Image.Resampling.LANCZOS` for high-quality downsampling and `optimize=True, quality=95` for efficient storage.

### 🛠️ Technologies Used

* **Backend:** Django (Python Web Framework), Django Signals
* **Image Processing:** Pillow (Python Imaging Library fork)
* **File Storage:** Django's `ImageField` and media file handling.

---

## 📧 Email OTP Sending

The "Email OTP Sending" project demonstrates how to implement a custom user model in Django and integrate email-based One-Time Password (OTP) authentication for user login. This project moves away from traditional username/password authentication by allowing users to log in using their phone number (acting as the primary identifier) and a dynamically generated OTP sent to their associated email.

This project delves into:

* **Custom User Model:** Implementing `AbstractUser` and a custom `UserManager` to define a user model with `phone_number` as the `USERNAME_FIELD`.
* **Email Integration:** Sending emails using Django's built-in `send_mail` function, configured with an SMTP backend (e.g., Gmail).
* **OTP Generation & Verification:** Generating random OTPs, storing them, and verifying them for user authentication.
* **Secure Authentication Flow:** A basic, yet functional, OTP-based login process, with considerations for security (though production-grade systems would require more robust measures like rate limiting, expiry, etc.).

### ✨ Features

The Email OTP Sending project includes the following core functionalities:

* **Phone Number Based Login:** Users initiate login by providing their registered phone number.
* **OTP Generation:** A random 4-digit OTP is generated for the user.
* **Email OTP Delivery:** The generated OTP is sent to the email address associated with the user's phone number.
* **OTP Verification:** Users enter the received OTP to complete the login process.
* **Dashboard Access:** Successful OTP verification grants access to a protected dashboard.
* **Logout Functionality:** Securely logs the user out of their session.
* **Custom User Model:** The application utilizes a custom user model where `phone_number` is the unique identifier, replacing the default `username`.

### 🛠️ Technologies Used

* **Backend:** Django (Python Web Framework), Django's Custom User Model, Django's Email Backend.
* **Database:** PostgreSQL (using `psycopg2` for connectivity).
* **Email Service:** Configured to use SMTP (e.g., Gmail's SMTP server).
* **Frontend (HTML/CSS):** Basic HTML templates with Bootstrap for minimal styling.

### ⚠️ Security Considerations (for production use)

* **Email Credentials:** `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` are hardcoded in `settings.py`. For production, these **MUST** be loaded from environment variables (e.g., using `python-decouple` or `django-environ`) and never committed to version control.
* **2-Factor Authentication (2FA) for Sender Email:** If your sender email (e.g., Gmail) has 2FA enabled, you'll need to generate an "App password" and use that instead of your regular email password. Instructions for this are noted in the project's `settings.py`.
* **OTP Robustness:** For a production system, consider:
    * OTP expiry (e.g., 5-10 minutes).
    * Rate limiting for OTP requests to prevent abuse.
    * More secure OTP generation (e.g., using Django's built-in `secrets` module or a dedicated OTP library).
    * Handling invalid phone numbers or emails more gracefully.

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
