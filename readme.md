# 구글 드라이브의 파일명을 일괄로 바꾸자.

- [Google Drive API Docs](https://developers.google.com/drive/api/guides/about-sdk?hl=ko)
- [Google Drive API Reference (v3)](https://developers.google.com/drive/api/reference/rest/v3?hl=ko)

## 기능


## API Setup

### pip install

```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 인증정보를 생성해야 함.

#### 1. API 사용 동의

[[Google Drive API]](https://console.cloud.google.com/flows/enableapi?apiid=drive.googleapis.com&hl=ko) 사용 설정 하기

#### 2. OAuth 동의 화면 구성

API 및 서비스 > [[OAuth 동의 화면 구성]](https://console.cloud.google.com/apis/credentials/consent?hl=ko) 에서 외부 사용자로 생성한다.
- **범위**에서 Drive 범위를 추가한다.
- 파일 조회하고 이름변경 하려는 기능(`list`, `update`)은 `/auth/drive.metadata`만 있으면 됨.
- 테스트 사용자는 본인의 구글 계정으로 하면 된다.

#### 3. 사용자 인증 정보 생성

[[사용자 인증 정보]](https://console.cloud.google.com/apis/credentials?hl=ko)에서 **OAuth 클라이언트 ID**를 생성

- 애플리케이션 유형은 **데스크톱 앱**으로 생성
- 이름만 적당히 주고, JSON파일을 저장하여 `credentials.json`으로 이름을 변경하여 사용

#### 끗
