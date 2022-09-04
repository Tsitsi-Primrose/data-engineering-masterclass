python -m tsitsi_test \
  --project $PROJECT_NAME \
  --cb_project_id $PROJECT_NAME \
  --runner DataflowRunner \
  --region europe-west1 \
  --worker_zone europe-west1-b \
  --max_num_workers 1 \
  --staging_location gs://$BUCKET_NAME/staging \
  --temp_location gs://$BUCKET_NAME/temp \
  --input_mode stream \
  --input_topic projects/$PROJECT_NAME/topics/$PUBSUB_TOPIC \
  --output_dataset $DATASET \
  --output_table $TABLE \
  --autoscaling_algorithm=THROUGHPUT_BASED \
  --job_name tsitsi_test \
  --experiment=use_beam_bq_sink \
  --transform_name_mapping='{"ReadInput":"ReadInput", "Parse":"Parse", "Transform":"Transform", "Write to Table":"Write to Table"}' \
  --update

  