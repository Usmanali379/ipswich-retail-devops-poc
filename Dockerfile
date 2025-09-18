FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# make the start script executable
RUN chmod +x /app/render_start.sh

ENV DJANGO_SETTINGS_MODULE=ipswich_shop.settings
ENV PORT=8000

EXPOSE 8000
CMD ["./render_start.sh"]