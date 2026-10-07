FROM --platform=linux/amd64 python:3.12
WORKDIR /app
COPY wheels /wheels
RUN python -m pip install --no-index --find-links=/wheels foundry-compute-modules
COPY app.py logic.py /app/
USER 5000
CMD ["python", "app.py"]
