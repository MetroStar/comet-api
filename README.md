# Welcome to the Comet API!

The goal of this project is to provide a Python-based starter API, which comes pre-configured with tools supporting the accelerated development of both Comet as well as general python APIs. Some of these tools are as follows:

- Platform: Python
- Web Framework: Fast API
- Database: SQLite, Alembic
- ORM: SQLAlchemy
- Data Validation: Pydantic
- Unit Testing: PyTest
- Code Quality: Ruff, PyLint, Black, isort
- Authentication support: JWT (coming soon)
- Documentation: Swagger and ReDoc

## Table of Contents

1. [Running the Project Locally](#running-the-project-locally)
2. [Running Unit Tests](#running-unit-tests)
3. [Running Code Quality Checks](#running-code-quality-checks)
4. [Contributing](#contributing)

## Running the Project Locally

1. To create an environment, run the following:

```sh
virtualenv -p python3 venv
source venv/bin/activate
```

2. To install dependencies, run the following:

```sh
pip install -r requirements.txt
```

3. To prepare your environment, add a file called `.env` to the `comet-api` directory. Copy and paste the template below and replace the placeholder values with your own:

```
DATABASE_URL=[SOME_URL] # Ex: 'sqlite:///./db.sqlite3'
```

4. To start the app, run the following:

```sh
uvicorn app.main:app --reload --host=0.0.0.0 --port=5000
```

## Running Unit Tests

1. To run unit tests, run the following:

```sh
pytest
```

2. To run unit tests with code coverage, run the following:

```sh
coverage run -m pytest && coverage html
```

## Running Code Quality Checks

1. To run code quality checks, run the following:

```sh
ruff check .
```

## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature_a`)
3. Commit your Changes (`git commit -m 'Added new feature_a'`)
4. Push to the Branch (`git push origin feature_a`)
5. Open a Pull Request
