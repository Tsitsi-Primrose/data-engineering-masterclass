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
PROJECT_NAME=
PUBSUB_TOPIC=
DATASET=
TABLE=
BUCKET_NAME=
REGION=
ZONE=
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
# data-engineering-masterclass
