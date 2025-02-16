# CONTRIBUTING

## How to run the Dockerfile locally


```bash
docker run --name=flask-api --detach --publish -w /app -v "$(pwd):/app" flask-smorest-api:latest sh -c "flask run --host 0.0.0.0"
```
