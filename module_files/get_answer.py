import json
import requests


def generate_response(question, *args):
    """
    直接传用户输入的问题就行，llm自动会进行解答
    :param question:
    :param args:
    :return: {"query": "", 'result': "" }
    """
    URL = "http://qa.inner.lymboy.com?q="
    if not question:
        return None
    if question is list:
        question = " ".join(question)

    # 发送请求
    res = requests.get(URL + question)
    res = json.loads(res.content.decode('unicode-escape'), strict=False)
    return res['result']


if __name__ == '__main__':
    test = generate_response("云计算服务")
    print(test)
    print('\n')
    print(type(test))
