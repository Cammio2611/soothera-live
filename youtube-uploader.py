import os
import glob
import time
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate_youtube():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("client_id.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)

def upload_video(youtube, file_path, title, description):
    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["Soothera", "wellness", "headache", "relief", "Shorts"],
            "categoryId": "22"  # People & Blogs
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False,
        }
    }

    media = MediaFileUpload(file_path, mimetype="video/mp4", resumable=True)
    response = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    ).execute()

    print(f"✅ Uploaded: {response['id']}")

if __name__ == "__main__":
    youtube = authenticate_youtube()

    # Use latest video in /videos/ directory
    video_files = sorted(glob.glob("videos/*.mp4"), reverse=True)
    if not video_files:
        print("❌ No videos found to upload.")
        exit()

    latest = video_files[0]
    title = "Natural Migraine Relief Tips #Shorts"
    description = "Quick natural tips to ease migraines in 2025. #Soothera #Shorts"

    upload_video(youtube, latest, title, description)
