import streamlit as st


# 用户输入问题
def user_message(input_text):
    with st.chat_message("user"):
        st.write(input_text)


# 以往回答结果
def old_messages(output_text):
    with st.chat_message("assistant"):
        st.write(output_text)


# 获取chatgpt接口返回的结果
def chatgpt_message(text):
    # 测试用
    output_text = "chatgpt对问题：【" + text + "】的回答结果"
    with st.chat_message("assistant"):
        st.write(output_text)
        return output_text
    # 实际调用
    # output_text = 第4步调用函数（）
    # with st.chat_message("assistant"):
    #     st.write(output_text)
    #     return output_text
