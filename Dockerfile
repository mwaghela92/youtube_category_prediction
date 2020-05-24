From python:3.6.10
Copy requirements.txt /code/requirements.txt
WORKDIR /code/
RUN pip install -r requirements.txt
COPY dev_youtube.py /code/dev_youtube.py
COPY function_process_sentence.py /code/function_process_sentence.py
COPY trained_model.sav /code/trained_model.sav
COPY vectorizer_file.sav /code/vectorizer_file.sav
ENTRYPOINT ["python"]
CMD ["dev_youtube.py"]