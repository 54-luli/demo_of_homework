import os
import sys

sys.path.append(os.getcwd())

from module_files.front_functions import *
from module_files.keywords import *
from module_files.get_answer import *


def test_modules(module):
    prompt = st.chat_input("请输入您想查询的问题")
    if module == '关键词提取模块':
        # prompt = st.chat_input("请输入您想查询的问题")
        # 用户输入问题的关键词提取函数测试
        if prompt:
            # 首次回答
            if not st.session_state:
                user_message(prompt)
                key_words1 = extract_keywords(prompt)
                result1 = chatgpt_message(key_words1, 1)
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
                result2 = chatgpt_message(key_words2, 1)
                # 保存最新一次回答
                st.session_state.user.append(prompt)
                st.session_state.ans.append(result2)
    elif module == '关键词相关文档链接获取模块':
        # prompt = st.chat_input("请输入您想查询的问题")
        # 用户输入问题的关键词提取函数测试
        if prompt:
            # 首次回答
            if not st.session_state:
                user_message(prompt)
                result1 = get_result(prompt)
                st.session_state.user = [prompt]  # 新建用户输入问题存储列表
                st.session_state.ans = [result1]  # 新建以往回答结果存储列表
            else:
                # 列表展示以往回答
                for i in range(len(st.session_state.user)):
                    user_message(st.session_state.user[i])
                    old_messages(st.session_state.ans[i])
                # 展示最新一次回答
                user_message(prompt)
                result2 = get_result(prompt)
                # 保存最新一次回答
                st.session_state.user.append(prompt)
                st.session_state.ans.append(result2)
    elif module == '生成结果模块':
        # prompt = st.chat_input("请输入您想查询的问题")
        # 用户输入问题的关键词提取函数测试
        if prompt:
            # 首次回答
            if not st.session_state:
                user_message(prompt)
                ans1 = generate_response(prompt)
                result1 = chatgpt_message(ans1, 3)
                st.session_state.user = [prompt]  # 新建用户输入问题存储列表
                st.session_state.ans = [result1]  # 新建以往回答结果存储列表
            else:
                # 列表展示以往回答
                for i in range(len(st.session_state.user)):
                    user_message(st.session_state.user[i])
                    old_messages(st.session_state.ans[i])
                # 展示最新一次回答
                user_message(prompt)
                ans2 = generate_response(prompt)
                result2 = chatgpt_message(ans2, 3)
                # 保存最新一次回答
                st.session_state.user.append(prompt)
                st.session_state.ans.append(result2)
