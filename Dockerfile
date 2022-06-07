FROM python:3.8

ENV PYTHONDONTWHRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#WORKDIR ../djangoProject
##WORKDIR /usr/src/djangoProject
#WORKDIR D:/PycharmProjects/djangoProject
##COPY  ./Group/req.txt /usr/src/req.txt
#RUN install --upgrade pip
#COPY ./Group/req.txt .
#COPY ./Group/req.txt C:/PycharmProjects/req.txt
#RUN pip install -r C:/Users/helen/PycharmProjects/req.txt
##RUN pip install -r /usr/src/req.txt
#RUN pip install --upgrade pip && pip install -r req.txt
#ADD . /web_django/
#COPY . D:/PycharmProjects/djangoProject
##COPY . /usr/src/djangoProject



#WORKDIR C:/Users/helen/PycharmProjects/djangoProject
#COPY  ./req.txt C:/Users/helen/PycharmProjects/djangoProject/req.txt
#RUN pip install -r C:/Users/helen/PycharmProjects/djangoProject/req.txt
#COPY . C:/Users/helen/PycharmProjects/djangoProject

#WORKDIR C:/Users/helen/PycharmProjects/djangoProject
#COPY  C:/Users/helen/PycharmProjects/djangoProject/req.txt .
#RUN pip install -r req.txt
#COPY . C:/Users/helen/PycharmProjects/djangoProject

#WORKDIR ../djangoProject
#COPY  ./req.txt .
#RUN pip install -r req.txt
#COPY ../djangoProject .


WORKDIR /app
ADD . /app
RUN pip install -r req.txt
#COPY ../djangoProject .

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]