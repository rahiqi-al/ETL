FROM python:3.10.12

WORKDIR /ETL_PROJECT

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python","elt_pipeline.py" ]
