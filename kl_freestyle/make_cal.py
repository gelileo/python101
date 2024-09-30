from ics import Calendar, Event
from datetime import datetime, timedelta
from convert2json import convert_file_to_json
import pytz

"""
Explanation of localize():

When you create a datetime object in Python using datetime.strptime(), it does not have any associated timezone information. The datetime object is “naive,” meaning it represents the date and time, but without any notion of what time zone that time is in.

The localize() function provided by pytz is used to “attach” or associate the naive datetime object with a specific timezone—without changing the actual time. This allows the datetime object to become “timezone-aware,” which means it knows that the time you’re providing is in a specific timezone (e.g., America/New_York).

Here’s what happens step by step:

What localize() Does:

	1.	Naive datetime (start_dt):
	•	You create start_dt using datetime.strptime(), which parses the event date and time from your input.
	•	This datetime object represents the event time in local time, but it doesn’t actually know it’s in America/New_York or any other timezone—it just holds a time like 6:00 AM or 1:45 PM.
	•	For example, start_dt might be 2024-10-01 06:00:00, but it has no associated timezone.
	2.	localize(start_dt):
	•	When you call local_tz.localize(start_dt), you are telling Python, “this start_dt should be treated as being in the America/New_York timezone.”
	•	It does not change the time; it simply adds information that the time is now considered to be in the Eastern Time Zone (New York).
	•	So after calling localize(), the start_dt is now considered to be 6:00 AM in America/New_York.
	3.	Why is this necessary?
	•	When you later save the event to the .ical file, the library will need to convert the time to UTC for proper formatting. If your datetime object is “timezone-aware,” it knows what local time it is and can accurately convert it to UTC for the iCal format.
	•	Without localize(), the time would be assumed to be in UTC or could lead to confusion, as it would be treated as a “naive” time with no timezone context.

Example:

Let’s say your event is scheduled at 6:00 AM on October 1, 2024, in Eastern Time (America/New_York).

Before localize():

	•	start_dt = 2024-10-01 06:00:00 (no timezone)

After localize():

	•	start_dt_localized = 2024-10-01 06:00:00-04:00 (Eastern Daylight Time, UTC-4)

This now makes the datetime object aware that 6:00 AM is in America/New_York, which allows for proper conversion to other time zones if needed (like UTC).

What Happens After Localization:

	•	iCal Conversion: When the .ical file is generated, if no explicit timezone information is retained (or if you’re saving in UTC), the library will automatically convert 6:00 AM in America/New_York to 10:00 AM UTC, because New York is UTC-4 during daylight saving time.

So, localize() ensures that you are working with timezone-aware datetime objects, which are critical for accurate time conversion.

Summary:

	•	localize() attaches timezone information to the naive datetime object, telling Python that the time is in America/New_York.
	•	The actual time (e.g., 6:00 AM) remains the same, but it is now properly associated with a timezone.
	•	This enables correct conversion to UTC when saving the event to .ical, as iCal files typically use UTC by default.
"""


def add_event_to_calendar(calendar, event_data, timezone="America/New_York"):
    event = Event()
    event.name = event_data["Event"]

    # Parse the date and time for the event
    event_date = event_data["Date"]
    event_time = event_data["Time"]

    start_time, end_time = event_time.split(" - ")

    # Assuming the date format is "MMM DD" (e.g., "Oct 01"), add the current year
    current_year = datetime.now().year
    start_dt = datetime.strptime(
        f"{current_year} {event_date} {start_time}", "%Y %b %d %I:%M%p"
    )
    end_dt = datetime.strptime(
        f"{current_year} {event_date} {end_time}", "%Y %b %d %I:%M%p"
    )

    # Convert local time to the specified timezone
    local_tz = pytz.timezone(timezone)
    start_dt_localized = local_tz.localize(start_dt)
    end_dt_localized = local_tz.localize(end_dt)

    # Set event times using the localized datetime objects
    event.begin = start_dt_localized
    event.end = end_dt_localized

    # Add the event to the calendar
    calendar.events.add(event)


if __name__ == "__main__":
    input_path = "schedule.txt"  # event schedule file path
    output_ical_file = "freestyle.ics"  # Replace with desired output .ical file name

    calendar = Calendar()
    events = convert_file_to_json(input_path, output_json_file="schedule.json")
    for event in events:
        add_event_to_calendar(calendar, event)

    # Write to .ical file
    with open(output_ical_file, "w") as f:
        f.writelines(calendar)

    print(f"iCal file has been created: {output_ical_file}")
