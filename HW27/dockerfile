FROM selenium/standalone-chrome

USER root

LABEL authors="nikitabulankov"

WORKDIR /app

COPY requirements.txt .

RUN sudo apt-get update && apt-get install -y python3.10 python3-pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/allure-results

EXPOSE 5050

CMD ["pytest", "-s", "-v", "--alluredir=allure-results"]