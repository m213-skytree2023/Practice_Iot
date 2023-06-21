import win32com.client as wincl
import json
import requests
import urllib3
import random
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "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"

def chat(text,
         messages=None,
         settings="",
         max_tokens=2000,
         temperature=1.,
         top_p=.1,
         presence_penalty=0.,
         frequency_penalty=0.):
    # やり取りの管理
    messages = messages if messages is not None else []
    if settings and not messages:
        messages.append({"role": "system", "content": settings})
    messages.append({'role': 'user', 'content': text})
    # ヘッダ
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    # ペイロード
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty,
        "stream": True,
    }
    # APIを叩く、streamをTrueに
    resp = requests.post(API_URL, headers=headers, json=payload, stream=True, verify=False)
    # 返答を受け取り、逐次yield
    response_text = ''
    for chunk in resp.iter_lines():
        try:
            j = json.loads(chunk.decode()[6:])
            content = j['choices'][0]['delta'].get('content')
            if content:
                response_text += content
                yield content
        except:
            ...
    else:  #
        messages += [{'role': 'assistant', 'content': response_text}]
        
# resp = ""
# messages = []
# for talk in chat('こんにちは。自己紹介してください。', messages):
#     # print(talk, end='')
#     resp += talk
    
# print(resp)

def say(sentence):
    voice = wincl.Dispatch("SAPI.SpVoice")
    voice.Rate = -1
    voice.Speak(sentence)

talebook = ["人魚姫","みにくいアヒルの子","ティンかいかくとり","雪の女王",
            "親指姫","赤ずきん","おおかみと七ひきの子やぎ","おやゆびひめ",
            "葉っぱの服を着た野ねずみ","幸せな王子"]
    
def tell_tale():
    title = talebook[random.randint(0, 10)]
    ask = "眠る前に、子供に"+title+"の物語話しましょう,200字内で"
    print(ask)
    tale = ""
    messages = []
    for talk in chat(ask, messages):
        tale += talk
    
    print(tale)
    say(tale)
    
tell_tale()
# say(resp)
