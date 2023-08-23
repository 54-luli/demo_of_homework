import requests


def searchdoc(page, pagesize, keywords):
    url = "http://114.55.61.91:10087/searchDoc"
    data = {
        "page": page,
        "pageSize": pagesize,
        "keywords": keywords
    }
    response = requests.post(url, json=data)
    return response.text


if __name__ == '__main__':
    print(searchdoc(1, 20, ["云服务器", "镜像"]))
