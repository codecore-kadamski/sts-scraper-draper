FROM pypy:3

WORKDIR /app

ENV PATH="chromedriver-path:${PATH}:${PACKAGE_PATH}"
ENV PYTHONPATH=/app

RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY scrapper ./scrapper

CMD [ "pypy3", "./scrapper/engines.py" ]