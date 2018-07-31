"""
simple program to subtract time according to timezome"
"""

from datetime import datetime, timedelta
import pytz

if __name__ == "__main__":
  """
  """

  last_hour_date_time = datetime.now(tz=pytz.timezone('US/Eastern')) - timedelta(days = 1, hours = 1)
  print(last_hour_date_time.strftime('%Y-%m-%d %H:%M:%S'))
  last_hour_date_time = datetime.now() - timedelta(days = 1)
  print(last_hour_date_time.strftime('%Y-%m-%d %H:%M:%S'))

