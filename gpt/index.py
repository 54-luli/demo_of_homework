import json
import openai

openai.proxy = {'http': 'http://localhost:7890', 'https': 'http://localhost:7890'}

openai.api_key = "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"

def generate_response(question: str) -> str:
    """
    
    
    """
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
