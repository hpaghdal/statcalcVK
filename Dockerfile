FROM python:3

ADD . .
##src /src

RUN pip install coverage

CMD [ "python", "./Calculator/test_statistics.py" ]

#CMD ["python", "-m", "unittest", "discover", "-s", "Tests"]