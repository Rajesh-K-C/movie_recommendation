def format_minutes(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}h {mins}m"
