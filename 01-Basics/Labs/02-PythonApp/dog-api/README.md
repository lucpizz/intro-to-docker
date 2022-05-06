# FastAPI

Fast API is a growing library of tools for building blazing fast APIs.

This is a hello world example of Fast API.

# Getting Started

This project uses poetry for its dependency management.

```
$ poetry init
```

Then, we can install dependencies with:

```
$ poetry install
```

This will install all of the dependencies for this project from within the project directory and start a virtual environment.

You will now be able to run Web Server with:

```
$ uvicorn main:app --reload
```

If everything is setup correctly, you should see this in your logs: 

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Assignment

Dockerize the app and run it on a Docker container.

## Bonus

You can run the tests with:

```
$ pytest
```

You will notice that the tests are failing.

Make the changes to make them pass.


