import streamlit as st
from module_files.front_text import *
from module_files.front_functions import *

# streamlit run streamlit_app.py
if __name__ == '__main__':
    st.set_page_config(page_title="🦜🔗 金山云智能小助手")
    st.title('🦜🔗 金山云智能小助手')
    st.divider()
    st.subheader('请在下方对话框输入您的问题')

    # 侧边栏
    with st.sidebar:
        # 创建两列布局
        col1, col2 = st.columns([1, 1])
        # 在第一列中显示图片
        col1.image("./img/kc-logo.png", width=128, use_column_width=True)
        # 在第二列中显示标题
        col2.markdown(f"<h1 style='font-size:40px;transform:translateY(20px);'>{jinshanyun}</h1>",
                      unsafe_allow_html=True)

        # 欢迎语句
        with st.container():
            st.markdown(first_sentence)

        with st.expander("📚 计算资源", False):
            for line in computing_resource:
                st.markdown(line, unsafe_allow_html=True)

        with st.expander("📚 大数据", False):
            for line in big_data:
                st.markdown(line, unsafe_allow_html=True)

        with st.expander("📚 数据库", False):
            for line in database:
                st.markdown(line, unsafe_allow_html=True)

        with st.expander("📚 网络", False):
            for line in network:
                st.markdown(line, unsafe_allow_html=True)

        # 结束句
        with st.container():
            for line in last_sentence:
                st.markdown(line, unsafe_allow_html=True)

    prompt = st.chat_input("请输入您想查询的问题")
    if prompt:
        # 首次回答
        if not st.session_state:
            user_message(prompt)
            output1 = chatgpt_message(prompt, 3)
            st.session_state.user = [prompt]  # 新建用户输入问题存储列表
            st.session_state.ans = [output1]  # 新建以往回答结果存储列表
        else:
            # 列表展示以往回答
            for i in range(len(st.session_state.user)):
                user_message(st.session_state.user[i])
                old_messages(st.session_state.ans[i])
            # 展示最新一次回答
            user_message(prompt)
            output2 = chatgpt_message(prompt, 3)
            # 保存最新一次回答
            st.session_state.user.append(prompt)
            st.session_state.ans.append(output2)
