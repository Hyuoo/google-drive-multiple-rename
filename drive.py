from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

# 요청 할 API 사용 범위
SCOPES = [
    # "https://www.googleapis.com/auth/drive",
    # "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.metadata",
    # "https://www.googleapis.com/auth/drive.metadata.readonly",
    # "https://www.googleapis.com/auth/drive.appdata",
    # "https://www.googleapis.com/auth/drive.readonly",
]

# 적당히 필요한 mime type을 alias로써 넣어주기.
MIME_TYPE = {
    "mp4": "video/mp4",
    "folder": "application/vnd.google-apps.folder",
    "dir": "application/vnd.google-apps.folder",
    "text": "text/plain",
    "txt": "text/plain",
    "md": "text/markdown",
    "markdown": "text/markdown",
    "pdf": "application/pdf",
    "py": "text/x-python",
    "python": "text/x-python",
    "file": "application/vnd.google-apps.file",
    "sheet": "application/vnd.google-apps.spreadsheet",
    "gsheet": "application/vnd.google-apps.spreadsheet",
    "spreadsheet": "application/vnd.google-apps.spreadsheet",
    "csv": "text/csv",
    "json": "application/json",
    "zip": "application/x-zip-compressed",
    "png": "image/png"
}

class Drive:
    def __init__(self):
        self.service = self.get_service()
    
    def get_service(self):
        creds = None
        
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            service = build("drive", "v3", credentials=creds)
        except HttpError as error:
            print(f"eeee {error}")
        
        return service

    def get_file_list(self, *, page_size=20, repeat=0, mime_type=None, contains=None):
        """
        :param repeat: 0=infinite, count
        """
        # 검색 쿼리 생성
        q_fields = []

        # mimeType
        if type(mime_type) not in [list, tuple]:
            mime_type = [mime_type]
        for ft in mime_type:
            if ft[0] == "^":
                # ^으로 시작하면 일치하지 않는 파일
                operator = "!="
                value = MIME_TYPE.get(ft[1:], "")
            else:
                operator = "="
                value = MIME_TYPE.get(ft, "")
            
            if value:
                q_fields.append(f"mimeType{operator}'{value}'")
            else:
                msg = f"unexpected type:{ft}"
                raise ValueError(msg)
        
        # file name
        if type(contains) not in [list, tuple]:
            contains = [contains]
        for ct in contains:
            if ct[0] == "^":
                # ^으로 시작하면 포함되지 않은 파일.
                q_fields.append(f"not name contains '{ct[1:]}'")
            else:
                # contains가 포함 된 파일
                q_fields.append(f"name contains '{ct}'")
            

        files = []
        count = 0
        page_token = None
        q = " and ".join(q_fields)
        print(f"query: \"{q}\"")
        while (repeat == 0 or count != repeat):
            results = (
                self.service.files()
                .list(
                    q=q,
                    pageSize=page_size,
                    fields="nextPageToken, files(id, name, mimeType)",
                    pageToken=page_token
                    ).execute()
                )
            for f in results.get("files", []):
                print(f"found file: {f['name']}")
            files.extend(results.get("files", []))
            page_token = results.get("nextPageToken", None)
            if page_token is None:
                break
            count += 1
        
        return files

    def get_file(self, file_id):
        """
        :return: {'kind': 'drive#file', 'id': '19XFLIaadNjvIhca_lbHseMA9oIC31k5F', 'name': 'is_empty_file_0.txt', 'mimeType': 'text/plain'}
        """
        file = self.service.files().get(fileId=file_id).execute()
        return file

    def rename(self, file_id, new_name):
        """
        :return: {'kind': 'drive#file', 'id': '19XFLIaadNjvIhca_lbHseMA9oIC31k5F', 'name': 'is_empty_file_0p.txt', 'mimeType': 'text/plain'}
        """
        result = (
            self.service.files()
            .update(
                fileId=file_id,
                body={"name": new_name},
            ).execute()
        )

        return result
    

