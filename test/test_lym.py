import os
import sys
import openai

sys.path.append(os.getcwd())

from module_files.front_functions import *

# streamlit run streamlit_app.py
if __name__ == '__main__':
    st.set_page_config(page_title="🦜🔗 金山云智能小助手")
    st.title('🦜🔗 金山云智能小助手')

    os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = st.chat_input("请输入您想查询的问题")
    # 用户输入问题的关键词提取函数测试
    if prompt:
        ans = generate_response(prompt)
        # 首次回答
        if not st.session_state:
            user_message(prompt)
            result1 = chatgpt_message(ans, 1)
            st.session_state.user = [prompt]  # 新建用户输入问题存储列表
            st.session_state.ans = [result1]  # 新建以往回答结果存储列表
        else:
            # 列表展示以往回答
            for i in range(len(st.session_state.user)):
                user_message(st.session_state.user[i])
                old_messages(st.session_state.ans[i])
            # 展示最新一次回答
            user_message(prompt)
            result2 = chatgpt_message(ans, 1)
            # 保存最新一次回答
            st.session_state.user.append(prompt)
            st.session_state.ans.append(result2)

