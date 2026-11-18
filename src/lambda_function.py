import json
import urllib.request

ISS_API_URL = "http://api.open-notify.org/iss-now.json"


def lambda_handler(event, context):
    # Ask the public API for the current ISS location.
    with urllib.request.urlopen(ISS_API_URL, timeout=10) as response:
        data = json.load(response)

    # Report a failure if the API did not return a successful result.
    if data.get("message") != "success":
        raise ValueError("The ISS API did not return a successful response.")

    # Return the location data so we can see it in the Lambda test.
    return data