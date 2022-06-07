FROM python:3.8

ENV PYTHONDONTWHRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#WORKDIR ../djangoProject
##WORKDIR /usr/src/djangoProject
#WORKDIR D:/PycharmProjects/djangoProject
##COPY  ./Group/requirements.txt /usr/src/requirements.txt
#RUN install --upgrade pip
#COPY ./Group/requirements.txt .
#COPY ./Group/requirements.txt C:/PycharmProjects/requirements.txt
#RUN pip install -r C:/Users/helen/PycharmProjects/requirements.txt
##RUN pip install -r /usr/src/requirements.txt
#RUN pip install --upgrade pip && pip install -r requirements.txt
#ADD . /web_django/
#COPY . D:/PycharmProjects/djangoProject
##COPY . /usr/src/djangoProject



#WORKDIR C:/Users/helen/PycharmProjects/djangoProject
#COPY  ./requirements.txt C:/Users/helen/PycharmProjects/djangoProject/requirements.txt
#RUN pip install -r C:/Users/helen/PycharmProjects/djangoProject/requirements.txt
#COPY . C:/Users/helen/PycharmProjects/djangoProject

#WORKDIR C:/Users/helen/PycharmProjects/djangoProject
#COPY  C:/Users/helen/PycharmProjects/djangoProject/requirements.txt .
#RUN pip install -r requirements.txt
#COPY . C:/Users/helen/PycharmProjects/djangoProject

#WORKDIR ../djangoProject
#COPY  ./requirements.txt .
#RUN pip install -r requirements.txt
#COPY ../djangoProject .


WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
#COPY ../djangoProject .

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]