from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_transcript(url):
    try:
        # Extract video ID from URL
        video_id = extract_video_id(url)
        if not video_id:
            return "Error: Invalid YouTube URL"
        
        # Fetch transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Combine all transcript entries into a single text
        text = " ".join([entry["text"] for entry in transcript])
        
        return text
    except Exception as e:
        return f"Error: {str(e)}"

def extract_video_id(url):
    """Extract video ID from various YouTube URL formats"""
    patterns = [
        r'youtu\.be/([a-zA-Z0-9_-]{11})',
        r'youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})',
        r'youtube\.com/v/([a-zA-Z0-9_-]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None