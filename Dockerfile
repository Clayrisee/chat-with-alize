FROM python:3.9.16-slim-bullseye

RUN apt update -q && apt install -yq wget git

WORKDIR /app/

COPY requirements.txt /app/
COPY alize/ /app/alize/
COPY run_streamlit.sh /app/
COPY setup.py /app/
COPY main.py /app/

RUN cd /app/
RUN pip install --upgrade pip \
    && pip --default-timeout=1000 install --user -r requirements.txt \
    && pip install --user . \
    && pip install streamlit --force-reinstall

ENTRYPOINT ["/app/run_streamlit.sh"]