# define base image as python
FROM python:3.10


# install all packages for chromedriver: https://gist.github.com/varyonic/dea40abcf3dd891d204ef235c6e8dd79
 RUN apt-get update && \
     apt-get install -y xvfb gnupg wget curl unzip --no-install-recommends && \
     wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
     echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
     apt-get update -y && \
     apt-get install -y google-chrome-stable && \
     wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chromedriver-linux64.zip -O /tmp/chromedriver.zip && \
#     wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chrome-linux64.zip && \
     apt install unzip && \
     unzip /tmp/chromedriver* -d /chromedriver

#latest chrome driver compatibility is supposedly - 114.0.5735.90 ?
#https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chrome-linux64.zip

    
# make the chromedriver executable and move it to default selenium path.
 RUN chmod +x /chromedriver/chromedriver-linux64/chromedriver
 RUN mv /chromedriver/chromedriver-linux64/chromedriver /usr/bin/chromedriver


# copy the source code into /app 
 COPY . /app
 RUN pip install --upgrade --no-cache-dir -r ./app/requirements.txt
#RUN rm /requirements.txt # remove requirements file from container.




EXPOSE 80
# default entry point.
#CMD ["python", "app/headless_debian_selenium_chromedriver.py", "-c"]
#CMD ["/bin/bash"]
#NOTE:Must bind the django server process to 0.0.0.0 so that it listens on all network interfaces
CMD ["python", "/app/courtscraper/manage.py", "runserver", "0.0.0.0:80"]
