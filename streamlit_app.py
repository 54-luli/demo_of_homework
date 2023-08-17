import streamlit as st
# from langchain.llms import OpenAI


# openai_api_key = st.sidebar.text_input('OpenAI API Key')


# def generate_response(input_text):
#     llm = OpenAI(temperature=0.7, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
#     st.info(llm(input_text))
#
#
# with st.form('my_form'):
#     text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
#     submitted = st.form_submit_button('Submit')
#     if not openai_api_key.startswith('sk-'):
#         st.warning('Please enter your OpenAI API key!', icon='⚠')
#     if submitted and openai_api_key.startswith('sk-'):
#         generate_response(text)


# 用户输入问题
def user_message(input_text):
    with st.chat_message("user"):
        st.write(input_text)


# 以往回答结果
def old_messages(output_text):
    with st.chat_message("assistant"):
        st.write(output_text)


# 获取chatgpt接口返回的结果
def chatgpt_message(output_text):
    # 测试用
    with st.chat_message("assistant"):
        st.write(output_text)
        return output_text
    # 实际调用
    # output_text = 第4步调用函数（）
    # with st.chat_message("assistant"):
    #     st.write(output_text)
    #     return output_text


# streamlit run streamlit_app.py
if __name__ == '__main__':
    st.set_page_config(page_title="🦜🔗 Quickstart App")
    st.title('🦜🔗 Quickstart App')

    prompt = st.chat_input("请输入您想查询的问题")
    if prompt:
        tmp = ""
        # 首次回答
        if not st.session_state:
            user_message(prompt)
            output1 = chatgpt_message("chatgpt返回的第1次回答结果")
            st.session_state.user = [prompt]    # 用户输入问题存储列表
            st.session_state.ans = [output1]    # 以往回答结果存储列表
        else:
            # 列表展示以往回答
            for i in range(len(st.session_state.user)):
                user_message(st.session_state.user[i])
                tmp = "chatgpt返回的第" + str(i+2) + "次回答结果"    # 测试模拟
                old_messages(st.session_state.ans[i])
            # 展示最新一次回答
            user_message(prompt)
            output2 = chatgpt_message(tmp)
            # 保存最新一次回答
            st.session_state.user.append(prompt)
            st.session_state.ans.append(output2)

        # st.write(st.session_state.user)
        # st.write(st.session_state.ans)
