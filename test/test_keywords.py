import streamlit as st
from files.front_text import *
from files.front_functions import *
from keywords import *


# streamlit run streamlit_app.py
if __name__ == '__main__':
    st.set_page_config(page_title="🦜🔗 金山云智能小助手")
    st.title('🦜🔗 金山云智能小助手')

    # 侧边栏
    with st.sidebar:
        # 创建两列布局
        col1, col2 = st.columns([1, 1])
        # 在第一列中显示图片
        col1.image("./img/kc-logo.png", width=128, use_column_width=True)
        # 在第二列中显示标题
        col2.markdown(f"<h1 style='font-size:40px;transform:translateY(20px);'>{jinshanyun}</h1>",
                      unsafe_allow_html=True)
        for line in introductions_file:
            st.markdown(line)

    # 用户输入问题的关键词提取函数测试
    prompt = st.chat_input("请输入您想查询的问题")
    if prompt:
        user_message(prompt)
        output = extract_keywords(prompt)
        result = chatgpt_message(output)
