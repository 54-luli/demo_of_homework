# # 方法一：采用其他库来实现提取关键字
# import jieba
# from sklearn.feature_extraction.text import TfidfVectorizer
#
#
# sentence  = "能说说你对关系型数据库,非关系型数据库的理解吗,以及镜像的概念"
#
# # 对文本进行分词
# words = jieba.cut(sentence)
# words_str = " ".join(words)
#
#
# vectorizer = TfidfVectorizer()
# tfidf_matrix = vectorizer.fit_transform([words_str])
#
# # 获取关键字及其对应的TF-IDF值
# feature_names = vectorizer.get_feature_names_out()
# tfidf_scores = tfidf_matrix.toarray()[0]
#
# # 获取具有最高TF-IDF值的关键字
# keywords = [feature_names[i] for i in tfidf_scores.argsort()[-5:][::-1]]
# print(keywords)


###################################
# # jieba库提取关键字流程
# # 对文本进行分词
# words = jieba.cut(text)
#
# # 过滤停用词和非中文字符，并提取关键字
# # stopwords = set(['是', '一段', '示例', '文本', '我们', '希望', '从中', '提取'])
# # keywords = [word for word in words if word not in stopwords and len(word) > 1]
#
# mainwords = set(['关系型数据库','镜像'])
# keywords = [word for word in words if word in mainwords and len(word) > 1]
#
# print(keywords)
###################################


# 方法二： 使用chatgpt来实现提取关键字
import openai


def extract_keywords(input_text):
    # 初始化OpenAI的API客户端
    openai.api_key = "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"

    # 根据用户输入构建一个适当的提示
    prompt = f"提取以下文本的核心关键词：\n{input_text}\n关键词："

    # 调用GPT-3.5来生成关键词
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=5  # 根据需要设置关键词的最大数量
    )

    # 从GPT-3.5的响应中提取生成的关键词
    keywords = response.choices[0].text.strip()

    return keywords


if __name__ == '__main__':
    # 测试：调用函数并获取关键词
    input_text = "请你说说关系型数据，非关系型数据库的区别，以及镜像的基本原理"
    keywords = extract_keywords(input_text)
    print("提取的核心关键词：", keywords)
