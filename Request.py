import requests

url = 'https://www.ceskatelevize.cz/ivysilani/'

try:
    response = requests.get(url)
    response.raise_for_status()  # Wirft eine HTTPError-Ausnahme, wenn der HTTP-Statuscode einen Fehler anzeigt
    print('Statuscode:', response.status_code)
    # Füge hier weitere Verarbeitungsschritte hinzu, wenn die Anfrage erfolgreich war
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")