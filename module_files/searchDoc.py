import requests


def searchDoc(page, pageSize, keywords):
    url = "http://114.55.61.91:10087/searchDoc"
    data = {
        "page": page,
        "pageSize": pageSize,
        "keywords": keywords
    }
    response = requests.post(url, json=data)
    return response.text


print(searchDoc(1, 20, ["云服务器", "镜像"]))
