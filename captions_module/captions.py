from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def get_captions(video_id):

    try:
        print("Fetching captions for video ID:", video_id)
        transcript = YouTubeTranscriptApi.fetch(video_id, languages=['en'])
        captions = [item['text'] for item in transcript]
    except TranscriptsDisabled:
        captions = ["Captions are disabled for this video."]
    except NoTranscriptFound:
        captions = ["No transcript available for this video."]
    except Exception as e:
        captions = [f"An error occurred while fetching captions: {str(e)}"]

    return captions
    