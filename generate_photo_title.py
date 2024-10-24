import os
# from dotenv import load_dotenv
import base64
from openai import OpenAI

# load_dotenv()

def generate_photo_title(image, instruction):

    client = OpenAI()

    base64_image = base64.b64encode(image.read()).decode('utf-8')

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": f"""
                    너는 전문 사진 제목가야.
                    사진을 받으면 너는 [요청사항]을 보고 사진에 대한 제목을 지어주면 돼.
                    만약 [요청사항]에 별도의 내용이 없다면 그냥 사진을 보고 5가지 정도의 제목을 지어주면 돼.

                    [요청사항]
                    {instruction}
                """,
                },
                {
                "type": "image_url",
                "image_url": {
                    "url":  f"data:image/jpeg;base64,{base64_image}"
                },
                },
            ],
            }
        ],
        )
    return response.choices[0].message.content



# def analyze_image(card_image_url):
#     client = OpenAI()
#     response = requests.get(card_image_url)
#     if response.status_code == 200:
#         base64_image = base64.b64encode(response.content).decode('utf-8')
#     else:
#         raise Exception(f"Failed to fetch image from URL: {card_image_url}")

    