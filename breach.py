import hashlib
import requests


def check_breach(password):
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        return {"checked": False, "reason": "No internet connection."}
    except requests.exceptions.Timeout:
        return {"checked": False, "reason": "Request timed out."}
    except requests.exceptions.RequestException as e:
        return {"checked": False, "reason": str(e)}

    hashes = (line.split(":") for line in response.text.splitlines())

    for h, count in hashes:
        if h == suffix:
            return {"checked": True, "compromised": True, "count": int(count)}

    return {"checked": True, "compromised": False, "count": 0}