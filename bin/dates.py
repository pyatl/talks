#!/usr/bin/env python
"""Print a list of the dates for the 2nd Thursday of every month for a year.
"""

from __future__ import print_function

import argparse
import calendar
import datetime


ap = argparse.ArgumentParser()
ap.add_argument(
    'year',
    type=int,
    nargs='?',
    default=datetime.date.today().year,
    help='the year',
)
args = ap.parse_args()


# Show every month
for month in range(1, 13):

    # Compute the dates for each week that overlaps the month
    c = calendar.monthcalendar(args.year, month)
    first_week = c[0]
    second_week = c[1]
    third_week = c[2]

    # If there is a Thursday in the first week, the second Thursday
    # is in the second week.  Otherwise, the second Thursday must
    # be in the third week.
    if first_week[calendar.THURSDAY]:
        meeting_date = second_week[calendar.THURSDAY]
    else:
        meeting_date = third_week[calendar.THURSDAY]

    print('%3s: %2s' % (calendar.month_abbr[month], meeting_date))
