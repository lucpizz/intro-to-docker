# Flask PG 

This is an example of a server and a database running on the same machine using Docker Compose.

Within the root of this project, run the following command:

```console
docker-compose up -d
```

This will launch the application and the database in the background.

While both containers are running, you will need to locate the POSTGRES environment variables within the docker compose file and add these files to a .env file.

Restart the application by running the following command:

```console
docker-compose restart
```

You should now be able to access the application at the following URL:

```console
http://localhost:5000/
```



