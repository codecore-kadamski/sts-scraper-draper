FROM alpine:3.10

ENV CHROMEDRIVER_PORT 4444
ENV CHROMEDRIVER_URL_BASE ""
ENV CHROMEDRIVER_WHITELISTED_IPS ""

RUN apk add --no-cache bash chromium chromium-chromedriver

CMD [ "sh", "-c", "chromedriver --port=$CHROMEDRIVER_PORT --url-base=$CHROMEDRIVER_URL_BASE --whitelisted-ips=$CHROMEDRIVER_WHITELISTED_IPS" ]