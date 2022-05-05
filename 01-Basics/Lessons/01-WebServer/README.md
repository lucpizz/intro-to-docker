# Web Server and NGINX

Using containers is a common way to deploy web applications.

In this lab, we will download a container image for a web server and run it. We will then use that web server to host a simple web application.

## Download the Image

Within your terminal, run the following command:

```console
docker run --name nginx-lab -p 4000:80 -d nginx
```

What will this do?
- It will download the image for the container.
- It will create a container with the name `nginx-lab`.
- It will run the container on port 4000.
- It will run the container in the background.

Once the container is running, you can navigate to the URL:

```console
http://localhost:4000
```

You can also do this in your terminal using curl:

```console 
curl http://localhost:4000
```

You will get the nginx welcome page.

**What just happened?**