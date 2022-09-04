FROM python:3.7-slim

# Install JRE
RUN mkdir -p /usr/share/man/man1 /usr/share/man/man2 && \
    apt-get update &&\
    apt-get install -y --no-install-recommends openjdk-11-jre && \
    apt-get install ca-certificates-java -y && \
    apt-get clean && \
    update-ca-certificates -f;
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt ./requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . ./

ENTRYPOINT [ "python" ]

RUN python3 pipelines/postgres_batch.py



