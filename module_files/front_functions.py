import streamlit as st
from module_files.keywords import *
from module_files.searchdoc import *


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
    # 测试用
    output_text = "chatgpt对以上问题的的回答结果：\n" + answer
    with st.chat_message("assistant"):
        st.write(output_text)
        return output_text
    # 实际调用
    # output_text = 第4步调用函数（）
    # with st.chat_message("assistant"):
    #     st.write(output_text)
    #     return output_text


# 关键词提取与文档链接整合
def get_result(extract_prompt):
    output_keywords = extract_keywords(extract_prompt)
    keywords_of_url = searchdoc(1, 3, output_keywords)
    temp = f"\n关键词：{output_keywords}\n相关文档链接：{keywords_of_url}"
    result = chatgpt_message(temp)
    return result
