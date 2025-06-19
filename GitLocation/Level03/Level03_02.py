from datetime import datetime, timezone

print(datetime.now(timezone.utc))

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %p %A %B'))

print(datetime.now().strftime('%A, %B %d, %Y %H:%M:%S'))

print(datetime.now().strftime('%A, %b %x %r'))