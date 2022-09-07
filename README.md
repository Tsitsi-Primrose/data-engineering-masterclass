# Data Engineering masterclass

```bash
pip3 install virtualenv
```

```bash
virtualenv data_pipelines
```

```bash
source data_pipelines/bin/activate
```

(to deactivate virtual env)

```bash
source data_pipelines/bin/deactivate
```

Install dependendencies

```bash
pip3 install -r requirements.txt
```

```bash
export GOOGLE_APPLICATION_CREDENTIALS=.service-account/your-service-key
```

pip3 install --no-binary :all: grpcio --ignore-installed
pip3 install --no-binary :all: grpcio-tools --ignore-installed

For running locally, copy the variables underneath and paste them in your terminal. Then copy the contents of run-local.sh and paste them in terminal and run.

Give permission to sh scripts

```bash
chmod +x ./run-local.sh
chmod +x ./run-remote.sh
```

```bash
./run-local.sh
```

To deploy to dataflow
The variables are inside cloud build, under the trigger name 'cb-end-trip-order-dataflow-push-trigger' and we have ci/cd pipelines inside cloudbuild-dev.yaml and cloudbuild-prod.yaml that get triggered when we push to github to the developer and main branch respectively to deploy the pipeline.

```console
PROJECT_NAME=Masterclass
DATASET=masterclass
TABLE=batch_describe
```

```bash
./run-remote.sh
```

ALTER ROLE postgres password null;
https://supabase.com/pricing
docker pull postgres
docker pull mysql

docker build -t masterclass .
docker run -dp 3307:3307 masterclass
docker run -e MYSQL_ROOT_PASSWORD=tsitsi mysql
docker run masterclass

Create service account

- Create service account folder in root called .service-account

DBT setups

Check dbt is installed
dbt --version

dbt init masterclass

https://github.com/mtpatter/time-series-kafka-demo
https://towardsdatascience.com/make-a-mock-real-time-stream-of-data-with-python-and-kafka-7e5e23123582
https://florimond.dev/en/posts/2018/09/building-a-streaming-fraud-detection-system-with-kafka-and-python/
https://blog.logrocket.com/apache-kafka-real-time-data-streaming-app/

Relational database demo
SQL crush course:
Firstly sign up on github: https://github.com/join
Go to https://supabase.com/ and sign up using your github account

Go to https://colab.research.google.com/drive/1_UHtQN8BXN0NsvCLZoHVuck54Ma14KzB?authuser=1#scrollTo=S4Nt3Ud-923X for our notebook

RabbitMQ
https://www.rabbitmq.com/tutorials/tutorial-one-python.html
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
python3 streaming_pipelines/send.py

Listing queues
You may wish to see what queues RabbitMQ has and how many messages are in them. You can do it (as a privileged user) using the rabbitmqctl tool:

sudo rabbitmqctl list_queues
On Windows, omit the sudo:

rabbitmqctl.bat list_queues
