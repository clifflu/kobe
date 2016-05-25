import requests

URL = "http://curl.kobe.ga"

def submit(msg, format="text"):
    if format == "text":
        url = URL
    elif format == "image":
        url = "%s/img" % URL
    else:
        raise ValueError("Unknown format `%s`, expecting 'text' or 'image'" % msg)

    return requests.post(
        url=url,
        params={"format": "json"},
        data={"message": msg},
    )
