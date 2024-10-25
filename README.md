# photo-title-generator

GPT 유료 버전을 사용하지 않으시는 분들을 위해 만들어드린 간단한 사진 제목 생성 도구입니다.
A simple tool created for those who don't use the paid version of GPT to help generate photo titles.

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
