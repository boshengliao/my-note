FROM your_image:latest

ADD . /app
EXPOSE 5000/tcp

ENV FLASK_ENV "production"

CMD ["gunicorn", "-c", "gun.py", "app.app:app"]