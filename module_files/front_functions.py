import streamlit as st
from module_files.keywords import *
from module_files.searchdoc import *
from module_files.get_answer import *
from threading import Thread


# 用户输入问题
def user_message(input_text):
    with st.chat_message("user"):
        st.write(input_text)


# 以往回答结果
def old_messages(past_answer):
    with st.chat_message("assistant"):
        st.write(past_answer)


# 获取chatgpt接口返回的结果
def chatgpt_message(answer):
    with st.chat_message("assistant"):
        st.write(answer)
        return answer


# 关键词提取与文档链接整合
def get_result(extract_prompt):
    output_keywords = extract_keywords(extract_prompt)
    keywords_of_url = searchdoc(1, 1, output_keywords)
    temp = [output_keywords, keywords_of_url]
    result = chatgpt_message(temp)
    return result


def get_keywords_and_url(extract_prompt):
    output_keywords = extract_keywords(extract_prompt)
    keywords_of_url = searchdoc(1, 1, output_keywords)
    ans = "\n" + keywords_of_url
    # temp = [output_keywords, keywords_of_url]
    return ans


# 创建 Thread 的子类
class MyThread(Thread):
    def __init__(self, func, args):
        """
        :param func: 可调用的对象
        :param args: 可调用对象的参数
        """
        Thread.__init__(self)
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)

    def getresult(self):
        return self.result


def use_multi_threads(prompt):
    # 创建 Thread 实例
    t1 = MyThread(generate_response, args=(prompt,))
    t2 = MyThread(get_keywords_and_url, args=(prompt,))
    # 启动线程运行
    t1.start()
    t2.start()
    # 等待所有线程执行完毕
    t1.join()
    t2.join()
    # 获取线程中程序的运行结果
    tmp1, tmp2 = t1.getresult(), t2.getresult()
    ans = tmp1 + tmp2
    return ans
