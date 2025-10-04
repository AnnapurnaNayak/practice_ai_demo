# test_clean.py
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

video_id = 'KiB4eAeFRsw' 

try:
    # The correct, canonical call
    transcript = YouTubeTranscriptApi.fetch(video_id, languages=['en']) 

    # Process and confirm
    captions = [item['text'] for item in transcript]
    print("\n--- SUCCESS in CLEAN VENV ---")
    print(f"First line: {captions[0]}")

except Exception as e:
    print(f"\n--- ERROR in CLEAN VENV ---")
    print(f"Error: {e}")