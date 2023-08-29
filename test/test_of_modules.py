import os
import sys

sys.path.append(os.getcwd())

from module_files.front_functions import *
from module_files.keywords import *
from module_files.get_answer import *


def test_modules(module):
    prompt = st.chat_input("请输入您想查询的问题")
    if module == '关键词提取模块':
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
        # 打开页面还未提问时给出提问示例
        else:
            user_message("问题样例...")
            chatgpt_message("回答的答案样例...")
    elif module == '关键词相关文档链接获取模块':
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
        # 打开页面还未提问时给出提问示例
        else:
            user_message("问题样例...")
            chatgpt_message("回答的答案样例...")
    elif module == '生成结果模块':
        # 用户输入问题的关键词提取函数测试
        if prompt:
            # 首次回答
            if not st.session_state:
                user_message(prompt)
                ans1 = generate_response(prompt)
                result1 = chatgpt_message(ans1)
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
                result2 = chatgpt_message(ans2)
                # 保存最新一次回答
                st.session_state.user.append(prompt)
                st.session_state.ans.append(result2)
        # 打开页面还未提问时给出提问示例
        else:
            user_message("问题样例...")
            chatgpt_message("回答的答案样例...")
    elif module == '最终成品展示页面':
        # 用户输入问题的关键词提取函数测试
        if prompt:
            # 首次回答
            if not st.session_state:
                # user_message(prompt)
                # tmp1 = generate_response(prompt)
                # tmp2 = get_keywords_and_url(prompt)
                # ans1 = tmp1 + tmp2
                # result1 = chatgpt_message(ans1)
                # 多线程
                user_message(prompt)
                # 创建 Thread 实例
                t1 = MyThread(generate_response, args=(prompt,))
                t2 = MyThread(get_keywords_and_url, args=(prompt,))
                # 启动线程运行
                t1.start()
                t2.start()
                # 等待所有线程执行完毕
                t1.join()
                t2.join()
                # 获取线程中程序的运行结果
                tmp1, tmp2 = t1.getresult(), t2.getresult()
                ans1 = tmp1 + tmp2
                result1 = chatgpt_message(ans1)
                st.session_state.user = [prompt]  # 新建用户输入问题存储列表
                st.session_state.ans = [result1]  # 新建以往回答结果存储列表
            else:
                # 列表展示以往回答
                for i in range(len(st.session_state.user)):
                    user_message(st.session_state.user[i])
                    old_messages(st.session_state.ans[i])
                # # 展示最新一次回答
                # user_message(prompt)
                # tmp1 = generate_response(prompt)
                # tmp2 = get_keywords_and_url(prompt)
                # ans2 = tmp1 + tmp2
                # result2 = chatgpt_message(ans2)
                # # 保存最新一次回答
                # st.session_state.user.append(prompt)
                # st.session_state.ans.append(result2)
                # 多线程
                user_message(prompt)
                # 创建 Thread 实例
                t1 = MyThread(generate_response, args=(prompt,))
                t2 = MyThread(get_keywords_and_url, args=(prompt,))
                # 启动线程运行
                t1.start()
                t2.start()
                # 等待所有线程执行完毕
                t1.join()
                t2.join()
                # 获取线程中程序的运行结果
                tmp1, tmp2 = t1.getresult(), t2.getresult()
                ans2 = tmp1 + tmp2
                result2 = chatgpt_message(ans2)
                # 保存最新一次回答
                st.session_state.user.append(prompt)
                st.session_state.ans.append(result2)
        # 打开页面还未提问时给出提问示例
        else:
            user_message("问题样例...")
            chatgpt_message("回答的答案样例...")
