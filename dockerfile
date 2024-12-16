FROM python:3.10-slim
WORKDIR /docdir
COPY . .
RUN pip install pytest
CMD ["python", "todo.py"]