import requests

URL = "http://qa.inner.lymboy.com?q="


def generate_response(question: str | list[str], *args):
    """
    直接传用户输入的问题就行，llm自动会进行解答
    :param question:
    :param args:
    :return: {"query": "", 'result': "" }
    """

    if not question:
        return None
    if question is list:
        question = " ".join(question)

    # 发送请求
    res = requests.get(URL + question)

    return res.content.decode('unicode-escape')
