# Moneyworth

A simple web application built with Django for managing sales listings. Users can browse, create, and manage sales entries, view dashboards, and manage their profiles. The app features a modern UI with a navigation bar, hero section, and footer.

---

## Features

- User authentication (login/register)
- Dashboard for users
- Browse all sales listings
- Create new sale entries
- User profile management
- About and Contact pages
- Responsive design with Bootstrap

## Technologies Used

- Python 3
- Django
- Bootstrap 5

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd SDP_website
   ```
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv env
   .\env\Scripts\activate  # On Windows
   # Or on macOS/Linux:
   # source env/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   # Or, if requirements.txt is missing:
   pip install django
   ```
4. **Apply database migrations:**
   ```sh
   python sdp_project/manage.py migrate
   ```
5. **Run the development server:**
   ```sh
   python sdp_project/manage.py runserver
   ```

The application will be available at [http://localhost:8000/](http://localhost:8000/).

---

## Accessing Key Pages

- **Home:** [http://localhost:8000/](http://localhost:8000/)
- **Dashboard:** [http://localhost:8000/dashboard/](http://localhost:8000/dashboard/) _(loginrequired)_
- **Browse Sales:** [http://localhost:8000/sales/](http://localhost:8000/sales/)
- **Create Sale:** [http://localhost:8000/sales/create/](http://localhost:8000/sales/create/)
- **About:** [http://localhost:8000/about/](http://localhost:8000/about/)
- **Contact:** [http://localhost:8000/contact/](http://localhost:8000/contact/)

---

## Usage

- Register a new account or log in.
- Browse existing sales or create a new sale entry.
- Access your dashboard to manage your listings and profile.