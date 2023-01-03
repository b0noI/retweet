#!/bin/bash

docker build . -t gcr.io/social-investments-337201/retweet
docker push gcr.io/social-investments-337201/retweet
