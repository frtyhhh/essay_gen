from openai import OpenAI
import json

with open('api\prompt.json', 'r', encoding='utf-8') as file:
        # 加载 JSON 数据为 Python 列表
        data = json.load(file)

client = OpenAI(
    api_key = "f4cfca55-d9e6-4766-a9b9-219226e070c8",
    base_url = "https://ark.cn-beijing.volces.com/api/v3",
)
     
# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model = "deepseek-r1-250120",  # your model endpoint ID
    messages = data,
)

new_pair = {
        "role" : "assistant",
        "content" : "{}".format(completion.choices[0].message.content)
}

data.append(new_pair)

with open('api\prompt.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(completion.choices[0].message.content)
