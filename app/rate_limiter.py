from datetime import datetime, timedelta

RATE_LIMIT = 5
TIME_WINDOW = timedelta(minutes=1)

usage = {}

def check_rate_limit(api_key: str):
    now = datetime.utcnow()

    if api_key not in usage:
        usage[api_key] = []

    # remove old requests
    usage[api_key] = [
        t for t in usage[api_key]
        if now - t < TIME_WINDOW
    ]

    if len(usage[api_key]) >= RATE_LIMIT:
        return False

    usage[api_key].append(now)
    return True