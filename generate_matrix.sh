#!/bin/bash
# Generate a dynamic matrix input by retrieving every app directory containing
# a Dockerfile
# outputs the following:
#
# target:
#   - src: ./sqs/consumer
#     name: ./sqs/consumer/Dockerfile
#   - src: ./sqs/producer
#     name: ./sqs/producer/Dockerfile
targets=$(find -name Dockerfile)

echo "target:"
for target in $targets
do
    cat <<EOF
  - src: ${target%/*}
    name: $target
EOF
done
