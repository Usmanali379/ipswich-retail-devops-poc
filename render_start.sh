#!/usr/bin/env bash
set -eo pipefail

# DB schema
python manage.py migrate --noinput

# Static files for WhiteNoise
python manage.py collectstatic --noinput

# (Optional) seed demo data only when env var is set
if [ "${SEED_ON_START:-0}" = "1" ]; then
  python manage.py seed_products || true
fi

# Start the app
exec gunicorn ipswich_shop.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2