FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /hobbysite

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py migrate
RUN python manage.py collectstatic

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]