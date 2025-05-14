FROM selenium/standalone-chrome

LABEL authors="nikitabulankov"

ENV PYTHONPATH="/var/lib/jenkins/workspace/HW31"

USER root

WORKDIR /var/lib/jenkins/workspace/HW31

COPY requirements.txt /var/lib/jenkins/workspace/HW31/

RUN sudo apt-get update && apt-get install -y python3.10 python3-pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /var/lib/jenkins/workspace/HW31/

RUN mkdir -p /app/allure-results

CMD ["pytest", "-v", "--alluredir=allure-results"]
