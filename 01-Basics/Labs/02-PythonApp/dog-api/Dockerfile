# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

ENV LOG_LEVEL=debug

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt


WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
<<<<<<< HEAD
# CMD ["uvicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "dog-api.main:app"]

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]

=======
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]
>>>>>>> c1caf17d74ed8e0f90b905fe20f5c9f266ced692
# ENTRYPOINT ["/bin/sh"]