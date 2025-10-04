from flask import Flask, request, jsonify
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv() # Load environment variables from .env file
print("YOUTUBE_API_KEY:")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")  # Put your API key in environment variable
print("YOUTUBE_API_KEY:", YOUTUBE_API_KEY)
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

@app.route('/youtube-search', methods=['GET'])
def youtube_search_api(query, max_results=3):
    if not query:
        raise ValueError("Missing query parameter")

    search_response = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results
    ).execute()

    videos = []
    for item in search_response.get('items', []):
        video_id = item.get('id', {}).get('videoId')
        if not video_id:
            # skip if no videoId (could be channel or playlist)
            continue
        videos.append({
            'videoId': video_id,
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'url': f"https://www.youtube.com/watch?v={video_id}"
        })
    print ("Videos:", videos)
    return videos

if __name__ == '__main__':
    app.run(port=5001, debug=True)



