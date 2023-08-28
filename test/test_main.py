import os
import sys
import openai

sys.path.append(os.getcwd())

from module_files.front_text import *
from test_of_modules import *

# streamlit run streamlit_app.py
if __name__ == '__main__':
    st.set_page_config(page_title="🦜🔗 金山云智能小助手")
    st.title('🦜🔗 金山云智能小助手')
    st.divider()
    st.subheader('请在下方对话框输入您的问题')

    # st.write(sys.path)
    os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # 侧边栏
    with st.sidebar:
        option = st.selectbox(
            '#### 测试模块选择',
            ('关键词提取模块', '关键词相关文档链接获取模块'))

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

    if option == '关键词提取模块':
        test_modules('关键词提取模块')
    elif option == '关键词相关文档链接获取模块':
        test_modules('关键词相关文档链接获取模块')
    elif option == '生成结果模块':
        test_modules('生成结果模块')
