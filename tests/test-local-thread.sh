#!/bin/bash

curl -X POST -H "Content-Type: application/json" -d @thread-in.json http://127.0.0.1:8080/threadit
