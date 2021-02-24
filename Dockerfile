FROM python:3

COPY . /var/f5_project

WORKDIR /var/f5_project

RUN pip install -r requirements.txt
CMD ["python", "./run_tests.py"]

