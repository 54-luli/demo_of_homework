import json
import openai

# openai.verify_ssl_certs = False
openai.proxy = {'http': 'http://localhost:7890', 'https': 'http://localhost:7890'}

# openai.organization = "org-GizSlscEOzMKtpi9DTSeWfTI"
openai.api_key = "sk-xx"

# openai.api_version = "2023-05-15"

def answer_user_by_chatgpt(question: str) -> str:
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": question}
        ],
        max_tokens=999,
        temperature=0
    )
    resp_dic = json.loads(json.dumps(resp, ensure_ascii=False))
    
    if "choices" in resp_dic:
        return resp_dic["choices"][0]["message"]["content"]
    else:
        return "error"
