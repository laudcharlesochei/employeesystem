# employeesystem (Django)

This is a complete Django web application named **employeesystem** (replacing **employeeapp**) based on the practical steps in the uploaded manual.

## 1) Run locally (SQLite - easiest)

### A. Create & activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### B. Install dependencies

```bash
pip install -r requirements.txt
```

### C. Run migrations & create a user

```bash
python manage.py migrate
python manage.py createsuperuser
```

### D. Start the development server

```bash
python manage.py runserver
```

Open:
- Home: http://127.0.0.1:8000/
- Employees (requires login): http://127.0.0.1:8000/employees/
- Admin: http://127.0.0.1:8000/admin/

## 2) Optional: use MySQL (as in later labs)

Set environment variables before running `migrate`:

```bash
# Example
export DB_ENGINE=mysql
export DB_NAME=employee_db
export DB_USER=root
export DB_PASSWORD=your_password
export DB_HOST=localhost
export DB_PORT=3306
```

On Windows PowerShell:

```powershell
setx DB_ENGINE mysql
setx DB_NAME employee_db
setx DB_USER root
setx DB_PASSWORD your_password
setx DB_HOST localhost
setx DB_PORT 3306
```

Then:

```bash
pip install mysqlclient
python manage.py migrate
```

## Project structure
- `employeesystem/` – Django project settings/urls
- `employees/` – Django app (models, forms, views, templates, static)

