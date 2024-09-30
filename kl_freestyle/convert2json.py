import json


def convert_file_to_json(file_path, output_json_file=None):
    events = []

    # Read text from the file
    with open(file_path, "r") as file:
        lines = file.readlines()

    current_event = {}

    for i, line in enumerate(lines):
        if line.startswith("Event Name"):
            if current_event:  # If we already have an event, add it to the list
                events.append(current_event)
            current_event = {}
            current_event["Event"] = lines[i + 1].strip()
        elif line.startswith("Dates"):
            current_event["Date"] = lines[i + 1].strip()
        elif line.startswith("Days & Time"):
            current_event["Time"] = lines[i + 1].strip()

    # Add the last event
    if current_event:
        events.append(current_event)

    # return json.dumps(events, indent=4)
    if output_json_file:
        write_json_to_file(events, output_json_file)

    return events


def write_json_to_file(data, file_path):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
