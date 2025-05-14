package main

import (
	"context"
	"encoding/json"
	"log"

	"github.com/aws/aws-lambda-go/lambda"
)

func HandleBare(ctx context.Context, e *json.RawMessage) (json.RawMessage, error) {
	log.Printf("%s", *e)
	return *e, nil
}

func main() {
	lambda.Start(HandleBare)
}
