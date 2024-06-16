To run the application there must be proceed following steps:

1. Clone github repository:

    git clone https://github.com/danielkaz12/Django-Project.git

1. Create virtual enviroment:

    python3 -m venv .venv/portfolio

2. Activate virtual enviroment:

    source .venv/portfolio/bin/activate

3. Create docker container for postgres:

    docker run --name portfolio_postgresql -p 5432:5432 -e POSTGRES_DB=portfolio -e POSTGRES_USER=portfolio -e POSTGRES_PASSWORD=portfolio -d postgres:15-alpine

4. Run command to migrate existing migrations:

    python3 manage.py migrate

5. Run the application with:

    python3 manage.py runserver

6. Type the swagger endpoints in the browser under the url:

    http://localhost:8000/

## Tests

There is a posibility to run application tests. Project use pytest and it can be execute doing according steps:

    1. running script:

    ./run_tests.sh
