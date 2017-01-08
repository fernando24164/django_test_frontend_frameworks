import requests


def insertNewPlace():
    url = 'http://localhost:8080/api/places/add/'

    data = {
        "name": "Madrid2",
        "lat": "38.78",
        "longi": "-4.21",
    }

    response = requests.post(url=url, data=data)

    print response.text

if __name__ == '__main__':
    insertNewPlace()
