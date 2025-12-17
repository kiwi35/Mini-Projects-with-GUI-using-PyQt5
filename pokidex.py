import requests

base_url = "https://pokeapi.co/api/v2/"
def getinfo(name):
    url = base_url+f"/pokemon/{name}"
    data = requests.get(url)
    if data.status_code == 200:
        info = data.json()
        return info
    else:
        print("An error has occurred",data.status_code)
        return None

def main():
    print("Enter the name of the pokemon your are looking for in all small letters")
    pokemon_name = input("The name of the pokemon: ")
    data = getinfo(pokemon_name)
    if data:
        print(f"Name: {data["name"]}")
        print(f"height: {data["height"]}cm")
        print(f"weight: {data["weight"]}kgs")
        print(f"ID: {data["id"]}")

if __name__ == "__main__":
    main()




