# Labs

## 01-Exec

Within the directory, there is a Python API built with Fast API.

Your task is to complete the following: 

- Within the folder, there is a `static` folder with two HTML files. Creare routes within the `app.py` file to serve the files.
  -  `/` should return the `index.html` file.
  -  `/about` returns the `about.html` file.
- Fix the Dockerfile to run the container and properly return the two web pages


## 02-Ignore

Within the directory, there is a Python API built with Fast API.

Right now it coppies a lot of code that we don't need into the container. The container is bigger than it needs to be. This will lead to a lot of overhead.

Your task is to complete the following:
- Find a way to not containerize the code that we don't need.
- Fix the Dockerfile to run the container and properly return the two web pages.
