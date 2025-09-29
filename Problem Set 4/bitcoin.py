import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    f = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

api_key = "a241e10a551a9e1fbb575a28e38355a64d123a7220f06fa7a8d4add40ff74085"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.RequestException:
    sys.exit("Error fetching data from API")

data = response.json()
price = float(data["data"]["priceUsd"])
print(f"${f * price:,.4f}")



