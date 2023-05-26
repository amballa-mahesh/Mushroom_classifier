FROM python:3.11.3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python main.py


# docker build -t welcome-app .
# docker run -p 5000:5000 welcome-app