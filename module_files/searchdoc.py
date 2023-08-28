import requests
from urlextract import URLExtract


def searchdoc(page, pagesize, keywords):
    url = "http://114.55.61.91:10087/searchDoc"
    data = {
        "page": page,
        "pageSize": pagesize,
        "keywords": keywords
    }
    response = requests.post(url, json=data)
    # 直接返回接口查到的文本
    return response.text
    # 直接提取返回值里的地址链接
    # extractor = URLExtract()
    # urls = extractor.find_urls(response.text)
    # return urls


if __name__ == '__main__':
    print(searchdoc(1, 2, ["云服务器", "镜像"]))
