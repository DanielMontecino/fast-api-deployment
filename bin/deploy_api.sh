#!/bin/bash

repository=us-central1-docker.pkg.dev
project=alien-airfoil-417901
model_name=lg-api-registry
img_name=lg-api
version=latest
region=us-central1
image=$repository/$project/$model_name/$img_name:$version

gcloud config set project $project
gcloud config set run/region $region


echo "Building image"
docker build -t $repository/$project/$model_name/$img_name:$version .
docker image prune --force
docker push $repository/$project/$model_name/$img_name:$version

echo "Creating cloud run service"
gcloud run deploy lg-api-service \
  --image $repository/$project/$model_name/$img_name:$version \
  --platform managed \
  --region $region \
  --allow-unauthenticated
  
echo "Making a service publicly accessible"
gcloud run services add-iam-policy-binding lg-api-service \
    --member="allUsers" \
    --role="roles/run.invoker"


# get the URL of the cloud run service
url=$(gcloud run services describe lg-api-service --platform managed --region $region --format 'value(status.url)')

echo "API URL: $url"