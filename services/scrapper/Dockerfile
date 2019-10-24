FROM pypy:3

#ENV PYTHONPATH=/app

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

ARG PACKAGE_NAME=scrapper
ARG PACKAGE_PATH=/$PACKAGE_NAME
ENV PYTHONPATH=$PACKAGE_PATH
ENV PATH="chromedriver-path:${PATH}:${PACKAGE_PATH}"

#RUN mkdir -p $PACKAGE_PATH

RUN pip3 install --upgrade pip

WORKDIR $PACKAGE_PATH

COPY requirements.txt $PACKAGE_PATH

RUN pip install --no-cache-dir -r requirements.txt

#COPY .$PACKAGE_PATH $PACKAGE_PATH
COPY . .

#CMD [ "pypy3", "./scrapper/run.py" ]