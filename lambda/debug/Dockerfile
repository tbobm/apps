FROM golang:1.24 AS build

WORKDIR /app
# Copy dependencies list
COPY go.mod go.sum ./
# Build with optional lambda.norpc tag
COPY . .
RUN go build -tags lambda.norpc -o debug-lambda

# Copy artifacts to a clean image
FROM public.ecr.aws/lambda/provided:al2023 AS production

COPY --from=build /app/debug-lambda ./debug-lambda
ENTRYPOINT [ "./debug-lambda" ]

FROM production AS dev

RUN mkdir -p /aws-lambda-rie && \
    curl -Lo /aws-lambda-rie/aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie && \
    chmod +x /aws-lambda-rie/aws-lambda-rie

ENTRYPOINT [ "/aws-lambda-rie/aws-lambda-rie","./debug-lambda" ]

FROM production AS release
