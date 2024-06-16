 #!/bin/bash

echo Running tests...

# Set PYTHONPATH to include the directory containing your Django project
export PYTHONPATH=./portfolio:$PYTHONPATH

echo Creating test docker container...

export DJANGO_SETTINGS_MODULE=settings.tests

docker run --name pytest -p 5433:5432 -e POSTGRES_DB=pytest -e POSTGRES_USER=pytest -e POSTGRES_PASSWORD=pytest -d postgres:15-alpine

# Wait for PostgreSQL to be ready
echo Waiting for PostgreSQL to be ready...
until docker exec pytest pg_isready -U pytest -d pytest; do
  sleep 1
done
echo Running pytest...

pytest -vv

echo Removing postgres container for test...

docker rm -f pytest