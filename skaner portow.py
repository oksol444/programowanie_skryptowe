import socket
adres_ip = "192.168.0.1"
port_od = 20
port_do = 100
for port in range(port_od, port_do + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tworzenie gniazda TCP
    sock.settimeout(0.5)  #ustawiony timeout na 0.5 sekundy
    wynik = sock.connect_ex((adres_ip, port)) #sprawdzenie połączenia z portem

    if wynik == 0:
        print(f"Port {port} jest otwarty")
    else:
        print(f"Port {port} jest zamknięty")
    sock.close()
