import pandas as pd
import apache_beam as beam
from apache_beam.dataframe import convert
from apache_beam.io.jdbc import WriteToJdbc
from beam_mysql.connector.io import WriteToMySQL


outputs_prefix = 'outputs/part'
#df = pd.read_csv('./UCI_Credit_Card.csv', usecols=["ID","SEX"])


with beam.Pipeline() as pipeline:
  df = pd.read_csv('./iris.csv', nrows=1)
  (
      
      # Convert the Pandas DataFrame to a PCollection.
      convert.to_pcollection(df, pipeline=pipeline)

      # We get named tuples, we can convert them to dictionaries like this.
    | 'To dictionaries' >> beam.Map(lambda x: dict(x._asdict()))

    #   # Reshuffle to make sure parallelization is balanced.
    #   | 'Reshuffle' >> beam.Reshuffle()
    #   | 'Print' >> beam.Map(print)
      | 'Write' >> WriteToMySQL(
        host="host.docker.internal",
        database="test",
        table="iris",
        user="root",
        password="tsitsi",
        port=3307,
        batch_size=1000,
)
    #   | 'Write to Postgres jdbc' >> WriteToJdbc(
    #       table_name='de_masterclass_credit_card',
    #       driver_class_name='org.postgresql.Driver',
    #       jdbc_url='jdbc:postgresql://host.docker.internal:5433/postgres?user=postgres&password=tsitsi',
    #       #jdbc_url='jdbc:postgresql://db.bifupwqqdhrxhrzzuplr.supabase.co:5432/postgres',
    #       username='postgres',
    #       password='tsitsi'
    #     #|'Write' >> beam.io.WriteToText(outputs_prefix)
    # )
  )

      # Print the elements in the PCollection.
      #| 'Print' >> beam.Map(print)

  