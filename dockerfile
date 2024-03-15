FROM python:3.12

WORKDIR /python_web_HW1

COPY . .

ENTRYPOINT [ "python", "/python_web_HW1/personal_bot_assistant/personal_bot_assistant/personal_bot.py"]





