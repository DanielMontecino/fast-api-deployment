#!/bin/bash

docker build -t lg-api .
docker run -d -p 8080:8080 --name lg-api-container lg-api