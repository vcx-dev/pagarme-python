from datetime import datetime, timedelta

BULK_ANTICIPATION = {
    'payment_date': int(datetime.timestamp(datetime.now()+timedelta(days=3))*1000),
    'timeframe': 'start',
    'requested_amount': '500000',
    'build': 'true'
}

LIMITS = {
    'payment_date': int(datetime.timestamp(datetime.now()+timedelta(days=3))*1000),
    'timeframe': 'start'
}
