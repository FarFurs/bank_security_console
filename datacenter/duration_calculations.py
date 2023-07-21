from datetime import datetime, timezone, timedelta
import pytz


def is_visit_long(duration):
    if duration > timedelta(hours=1):
        return True
    else:
        return False


def get_duration(entered_at, leaved_at):
    if leaved_at is None:
        duration = datetime.now(pytz.timezone("utc")) - entered_at
    else:
        duration = leaved_at - entered_at
    return duration


def format_duration(duration):
    tz = timezone(timedelta(hours=3), name='МСК')
    format_duration = duration + tz.utcoffset(duration)
    return format_duration
