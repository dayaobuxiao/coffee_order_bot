import requests
import json

GLM4_API_ENDPOINT = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
API_KEY = "fa8169ddcea10641598540bf387bfc78.8L9Nr96gFTaR84ZQ"

def call_glm4_api(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "glm-4"
    }
    try:
        response = requests.post(GLM4_API_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()  # 抛出 HTTP 错误，如果有的话

        response_data = response.json()
        print("API Response:", response_data)  # 打印完整的 API 响应

        if 'choices' in response_data and len(response_data['choices']) > 0:
            return response_data['choices'][0]['message']['content'].strip()
        else:
            print("Unexpected API response structure:", response_data)
            return "抱歉，我现在无法回答。请稍后再试。"
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return "抱歉，发生了网络错误。请稍后再试。"
    except json.JSONDecodeError as e:
        print(f"Failed to parse API response: {e}")
        return "抱歉，处理响应时出错。请稍后再试。"
    except KeyError as e:
        print(f"Unexpected API response structure: {e}")
        return "抱歉，处理响应时出错。请稍后再试。"
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "抱歉，发生了未知错误。请稍后再试。"