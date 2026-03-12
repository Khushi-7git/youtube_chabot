# YouTube Bot 🎥

AI-powered chatbot that answers questions about YouTube videos using RAG (Retrieval Augmented Generation).

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Configure API key in config.py
GOOGLE_API_KEY = "your-api-key-here"

# Run the app
streamlit run app.py
```

## Features

- 📥 Load YouTube video transcripts automatically
- 💬 Ask questions about video content
- 🔍 Semantic search with FAISS vector store
- 🌐 Web search for additional information
- 🛠️ Built-in diagnostic tools

## Usage

1. **Load a video**: Enter YouTube URL and click "Load Video"
2. **Ask questions**: Chat with the bot about the video content
3. **Troubleshoot**: Use "Check Video" to verify transcript availability

## Test Videos

Videos with confirmed subtitles:
```
https://www.youtube.com/watch?v=Mus_vwhTCq0  (Short tech tutorial)
https://www.youtube.com/watch?v=8S0FDjFBj8o  (TED Talk)
https://www.youtube.com/watch?v=aircAruvnKk (Khan Academy)
```

## Troubleshooting

**"No element found" error?**
- Video doesn't have captions - use "Check Video" to verify
- Try a different video with confirmed subtitles

**"No transcripts found"?**
- Creator disabled captions for this video
- Use videos from educational channels (TED, Khan Academy, Crash Course)

## Configuration

Edit `config.py`:
```python
GOOGLE_API_KEY = "your-key"      # Get from Google AI Studio
MODEL_NAME = "gemini-pro"        # Or gemini-1.5-pro
CHUNK_SIZE = 1000                # Text chunk size
CHUNK_OVERLAP = 200              # Overlap between chunks
```

## Files

- `app.py` - Streamlit UI
- `agent.py` - LangChain agent
- `youtube.py` - Transcript fetching
- `rag.py` - Vector store & search
- `search.py` - Web search
- `test_youtube.py` - Diagnostic tool

## Requirements

- Python 3.8+
- Google API key (free at [Google AI Studio](https://makersuite.google.com/))
- Internet connection

## License

MIT
