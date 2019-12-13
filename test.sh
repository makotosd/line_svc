#!/bin/sh
#
#
#curl -X POST -H "Content-Type: application/json" -d @./test01.json localhost:8080/send_msg
curl -X POST -H "Content-Type: application/json" -d @./test02.json localhost:8080/send_msg