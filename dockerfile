FROM python:3.12

WORKDIR /python_web_HW1

COPY . .

ENTRYPOINT [ "python", "personal_bot.py" ]





