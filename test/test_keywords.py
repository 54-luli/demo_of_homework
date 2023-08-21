import os
import sys

sys.path.append(os.getcwd())

from files.front_text import *
from files.front_functions import *
from files.keywords import *

# streamlit run streamlit_app.py
if __name__ == '__main__':
    st.set_page_config(page_title="🦜🔗 金山云智能小助手")
    st.title('🦜🔗 金山云智能小助手')

    # st.write(sys.path)

    # 侧边栏
    with st.sidebar:
        openai_api_key = st.sidebar.text_input('请在下方输入您的OpenAI API key!')

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
    if not openai_api_key.startswith('sk-'):
        st.warning('请输入您的 OpenAI API key!', icon='⚠')
    # 用户输入问题的关键词提取函数测试
    elif prompt and openai_api_key.startswith('sk-'):
        user_message(prompt)
        output = extract_keywords(prompt, openai_api_key)
        result = chatgpt_message(output)
