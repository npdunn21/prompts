FROM python:3

WORKDIR /usr/src/app

COPY scripts makefile ./

COPY . .
RUN poetry install
CMD [ "python3", "./scripts/run_prompt_generator.py" ]