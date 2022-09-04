python -m order-end-trip \
  --project $PROJECT_NAME \
  --cb_project_id $PROJECT_NAME \
  --runner DirectRunner \
  --input_mode stream \
  --input_topic projects/$PROJECT_NAME/topics/$PUBSUB_TOPIC \
  --output_dataset $DATASET \
  --output_table $TABLE \
  --cb_compute local_compute \
  --experiment=use_beam_bq_sink 