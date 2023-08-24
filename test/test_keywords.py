import os
import sys
import openai
sys.path.append(os.getcwd())

from module_files.front_text import *
from module_files.front_functions import *


# streamlit run streamlit_app.py
if __name__ == '__main__':
    st.set_page_config(page_title="🦜🔗 金山云智能小助手")
    st.title('🦜🔗 金山云智能小助手')

    # st.write(sys.path)
    os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
    openai.api_key = os.getenv("OPENAI_API_KEY")

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

    prompt = st.chat_input("请输入您想查询的问题")
    # 用户输入问题的关键词提取函数测试
    if prompt:
        # 首次回答
        if not st.session_state:
            user_message(prompt)
            key_words1 = extract_keywords(prompt)
            result1 = chatgpt_message(key_words1)
            st.session_state.user = [prompt]  # 新建用户输入问题存储列表
            st.session_state.ans = [result1]  # 新建以往回答结果存储列表
        else:
            # 列表展示以往回答
            for i in range(len(st.session_state.user)):
                user_message(st.session_state.user[i])
                old_messages(st.session_state.ans[i])
            # 展示最新一次回答
            user_message(prompt)
            key_words2 = extract_keywords(prompt)
            result2 = chatgpt_message(key_words2)
            # 保存最新一次回答
            st.session_state.user.append(prompt)
            st.session_state.ans.append(result2)
