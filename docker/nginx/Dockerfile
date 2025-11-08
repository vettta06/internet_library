FROM nginx:alpine

COPY . /etc/nginx/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

CMD ["sh", "-c", "python manage.py migrate --noinput && \
                  python manage.py collectstatic --noinput && \
                  gunicorn --bind 0.0.0.0:8000 library_project.wsgi:application"]