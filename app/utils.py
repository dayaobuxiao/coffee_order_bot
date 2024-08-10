from app.llm_api import call_glm4_api

class CoffeeOrderAssistant:
    def __init__(self):
        self.context = []

    def process_input(self, user_input):
        # 将用户输入添加到上下文
        self.context.append(f"用户: {user_input}")

        # 构建提示
        prompt = """
        你是一个咖啡订购助手。请根据用户的输入，识别他们的意图，提取订单信息（如咖啡类型、温度、大小、数量、店铺、送达地址等），
        并以自然、友好的方式回应。如果信息不完整，请询问缺失的细节。当订单完成时，请总结订单并询问是否确认。

        以下是对话历史：
        """ + "\n".join(self.context[-5:])

        # 调用GLM4 API
        response = call_glm4_api(prompt)

        # 将助手回复添加到上下文
        self.context.append(f"助手: {response}")

        # 判断订单是否完成
        order_complete = "确认" in user_input or "正确" in user_input

        return {"response": response, "order_complete": order_complete}