# Host Static Site

We got the nginx web server running in the first lab, nice work!

NGINX is a popular web server that is used by many companies.

It is used because of its many features.

One of which is to host static content (no so different from Apache).

In this lab, we will use NGINX to host a static site.

## Getting Started

Within this directory, run the following command:

```console
docker build -t my-static-site .
```

This is going to build the image as it is defined in the Dockerfile. 

Now, run the following command:

```console
docker run --name my-static-site -p 3000:80 -d my-static-site
```

This will run the web server on port 3000.

If you visit the URL:

```console
http://localhost:3000
```

You will now see the webpage that you have defined in the `index.html` file in the `my_static_site` folder.


