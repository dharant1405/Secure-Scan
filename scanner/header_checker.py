import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options"
]


def check_headers(url):

    results = {}

    try:
        response = requests.get(url, timeout=5)

        headers = response.headers

        for header in SECURITY_HEADERS:
            results[header] = header in headers

        return results

    except Exception as e:
        return {"error": str(e)}