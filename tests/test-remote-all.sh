#!/bin/bash

curl -X POST -H "Content-Type: application/json" -d @test-in.json https://retweet-ewn37fowka-uc.a.run.app/rephrase
curl -H "Content-Type: application/json" https://retweet-ewn37fowka-uc.a.run.app/templates/DEFAULT
curl -H "Content-Type: application/json" https://retweet-ewn37fowka-uc.a.run.app/templates
curl -X POST -H "Content-Type: application/json" -d @thread-in.json https://retweet-ewn37fowka-uc.a.run.app/threadit
