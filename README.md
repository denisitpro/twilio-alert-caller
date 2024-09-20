# Twilio Caller Flask App

This is a simple Flask application that uses the Twilio API to make calls. The app is designed to run in a Docker container and can be easily deployed with a few environment variables.

## English

### Prerequisites
- Docker installed on your machine.
- A Twilio account with valid `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER`.

### Environment Variables
To run the application, you need to set the following environment variables:

- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID.
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token.
- `TWILIO_PHONE_NUMBER`: The Twilio phone number you want to use for calls.
- `TWIML_URL` (optional): URL for Twilio TwiML instructions (default: `https://handler.twilio.com/twiml/EH823a7a92d74a13a58da688bf18ffe7d2`).
- `TWILIO_PORT` (optional): The port on which the application will run (default: `5000`).
- `TWILIO_BIND_ADDRESS` (optional): The address to bind the application to (default: `0.0.0.0`).

### How to Run the Container

1. Pull the Docker image from Docker Hub:
    ```bash
    docker pull denisitpro/twilio-alert-caller:latest
    ```

2. Run the Docker container:
    ```bash
    docker run -e TWILIO_ACCOUNT_SID=your_account_sid \
               -e TWILIO_AUTH_TOKEN=your_auth_token \
               -e TWILIO_PHONE_NUMBER=your_twilio_phone_number \
               -e TWILIO_PORT=8080 \
               -p 8080:8080 \
               denisitpro/twilio-alert-caller:latest
    ```

The application will now be running on `http://localhost:8080`.

## Example curl command to make a test call

To make a test call using `curl`, run the following command:

```bash
curl -X POST http://localhost:8080/call \
     -H "Content-Type: application/json" \
     -d '{"to": "+1234567890"}'
```

## Русский 

### Требования
- Установленный Docker на вашем компьютере.
- Учетная запись Twilio с действующими значениями `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN` и `TWILIO_PHONE_NUMBER`.

### Переменные окружения
Для запуска приложения необходимо задать следующие переменные окружения:

- `TWILIO_ACCOUNT_SID`: Ваш Twilio Account SID.
- `TWILIO_AUTH_TOKEN`: Ваш Twilio Auth Token.
- `TWILIO_PHONE_NUMBER`: Телефонный номер Twilio, который вы хотите использовать для звонков.
- `TWIML_URL` (опционально): URL для инструкций TwiML от Twilio (по умолчанию: `https://handler.twilio.com/twiml/EH823a7a92d74a13a58da688bf18ffe7d2`).
- `TWILIO_PORT` (опционально): Порт, на котором будет запущено приложение (по умолчанию: `5000`).
- `TWILIO_BIND_ADDRESS` (опционально): Адрес, на который будет привязано приложение (по умолчанию: `0.0.0.0`).

### Как запустить контейнер

1. Загрузите Docker-образ с Docker Hub:
    ```bash
    docker pull denisitpro/twilio-alert-caller:latest
    ```

2. Запустите Docker-контейнер:
    ```bash
    docker run -e TWILIO_ACCOUNT_SID=ваш_account_sid \
               -e TWILIO_AUTH_TOKEN=ваш_auth_token \
               -e TWILIO_PHONE_NUMBER=ваш_twilio_phone_number \
               -e TWILIO_PORT=8080 \
               -p 8080:8080 \
               denisitpro/twilio-alert-caller:latest
    ```

Приложение теперь будет доступно по адресу `http://localhost:8080`.

## Пример команды curl для тестового звонка

Чтобы сделать тестовый звонок с использованием `curl`, выполните следующую команду:

```bash
curl -X POST http://localhost:8080/call \
     -H "Content-Type: application/json" \
     -d '{"to": "+1234567890"}'