# photo-title-generator

여자친구 어머님께서 사진 찍기를 좋아하시는데 GPT 유료 버전은 사용하지 않으셔서, 만들어드린 간단한 사진 제목 지어드리는 도구입니다.
My girlfriend's mother loves taking pictures, but since she doesn't use the paid version of GPT, this is a tool for her to generate photo titles.

## Setup

Create a Python Virtual Environment:
```
python -m venv venv
```

Enter Your Virtual Environment:
- For macOS/Linux:
```
source venv/bin/activate
```
- For Windows:
```
.\venv\Scripts\activate
```

To install the required packages:
```
pip install -r requirements.txt
```

Make sure you have a OpenAI API key and add it to the `.streamlit/secrets.toml` file. If you don't have one, sign up and get your API key from [OpenAI](https://platform.openai.com). For `authorization`, set a password of your choice; the tool will prompt you for that password when in use.
```
[general]
OPENAI_API_KEY = "[YOUR_OPENAI_API_KEY]"
authorization = "[PASSWORD_YOU_WANT]"
```
**Important**: Do not push the .streamlit/secrets.toml file to the Streamlit deployment. Instead, set it up in the advanced settings. Check out the [documentation](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) for more information.