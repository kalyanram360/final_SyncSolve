FROM python:3.11-slim

WORKDIR /app

# Install required system packages
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libxml2-dev \
    libxslt1-dev \
    libmysqlclient-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    default-libmysqlclient-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "syncsolve.wsgi:application", "--bind", "0.0.0.0:8000"]
