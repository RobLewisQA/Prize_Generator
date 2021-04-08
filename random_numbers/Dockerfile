FROM python:3.6
#RUN sudo apt install python3-pip #
COPY requirements.txt . 
RUN pip3 install -r requirements.txt 
COPY . . 
EXPOSE 5001
ENTRYPOINT ["python3","app.py"]