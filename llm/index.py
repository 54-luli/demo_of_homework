import os
import warnings

import pinecone
from langchain.chains import RetrievalQA
from langchain.chat_models.openai import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone

warnings.filterwarnings("ignore")

# os.environ["OPENAI_API_KEY"] = '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'
# os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

pinecone.init(
    api_key="bd95407b-37c9-4247-8026-4ea00e9eb271",
    environment="gcp-starter"
)

qa = None


def get_doc_dir():
    return os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..", "ksyun_docs"))


def init():
    # 加载文件夹中的所有pdf类型的文件
    loader = DirectoryLoader(get_doc_dir(), glob='**/*.pdf')
    # 将数据转成 document 对象，每个文件会作为一个 document
    documents = loader.load()

    # 初始化加载器
    text_splitter = CharacterTextSplitter(chunk_size=512, chunk_overlap=0)
    # 切割加载的 document
    split_docs = text_splitter.split_documents(documents)

    # 初始化 openai 的 embeddings 对象
    embeddings = OpenAIEmbeddings()
    # 将 document 通过 openai 的 embeddings 对象计算 embedding 向量信息并临时存入 Chroma 向量数据库，用于后续匹配查询
    docsearch = Pinecone.from_documents(split_docs, embeddings, index_name="langchain")
    # docsearch = Chroma.from_documents(split_docs, embeddings)

    # 创建问答对象
    return RetrievalQA.from_chain_type(llm=ChatOpenAI(), chain_type="stuff", retriever=docsearch.as_retriever(),
                                       return_source_documents=False)


def generate_response(question: str | list[str], *args):
    """
    直接传用户输入的问题就行，llm自动会进行解答
    :param question:
    :param args:
    :return: {"query": "", 'result': "" }
    """
    if question is list:
        question = str.join(question)
    global qa
    if not qa:
        qa = init()

    return qa({"query": question})
