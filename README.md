# Colabo Django REST API

This project is a Django REST Framework API for managing projects, tasks, and user authentication.

## Features

- User authentication (login, logout, signup)
- CRUD operations for projects
- CRUD operations for tasks associated with projects
- Custom permissions for accessing projects and tasks
- Integration with a Next.js frontend application

## Installation

1. Clone the repository:

```bash
git clone https://github.com/arshadbarves/colabo-api
cd colabo
```

2. Create a virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```

On macOS and Linux:

```bash
source venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Run the migrations:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

## Usage

1. **User Authentication:**

   - Use the `/api/auth/login/` endpoint to log in a user.
   - Use the `/api/auth/logout/` endpoint to log out a user.
   - Use the `/api/auth/signup/` endpoint to create a new user.

2. **Projects Endpoints:**

   - `/api/projects/`: List all projects or create a new project.
   - `/api/projects/<project-id>/`: Retrieve, update, or delete a specific project.

3. **Tasks Endpoints:**

   - `/api/tasks/`: List all tasks or create a new task.
   - `/api/tasks/<task-id>/`: Retrieve, update, or delete a specific task.

4. **Authentication Tokens:**

   - Include the authentication token in the `Authorization` header of requests to authenticate users when accessing protected endpoints.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

## License

This project is licensed under the Closed Source License - see the [LICENSE](LICENSE) file for details.
