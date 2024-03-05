# 구글 드라이브의 파일명을 일괄로 바꾸자.

> [Google Drive API Docs](https://developers.google.com/drive/api/guides/about-sdk?hl=ko)
> 
> [Google Drive API Reference (v3)](https://developers.google.com/drive/api/reference/rest/v3?hl=ko)

## API Setup

### pip install

```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 인증정보를 생성해야 함.

#### 1. API 사용 동의

[[Google Drive API]](https://console.cloud.google.com/flows/enableapi?apiid=drive.googleapis.com&hl=ko) 사용 설정 하기

#### 2. OAuth 동의 화면 구성

[[OAuth 동의 화면 구성]](https://console.cloud.google.com/apis/credentials/consent?hl=ko) 에서 외부 사용자로 생성한다.
- **범위**에서 Drive 범위를 추가한다.