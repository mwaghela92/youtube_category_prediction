FROM python:3.6.10
COPY requirements_model.txt /model/requirements_model.txt
WORKDIR /model/
RUN pip install -r requirements_model.txt
COPY model_training.py /model/model_training.py
ENTRYPOINT ["python"]
CMD ["model_training.py"]