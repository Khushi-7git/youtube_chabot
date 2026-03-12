from langchain.agents import AgentExecutor , create_react_agent
from langchain.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub
from youtube import get_transcript 
from rag import search_transcript, store_transcript
from config import GOOGLE_API_KEY, MODEL_NAME
from search import web_search
import os

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

llm=ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    temperature=0.7
)

# ✅ Single tool that fetches + stores in one shot
def load_and_store_video(url: str) -> str:
    url = url.strip()
    text = get_transcript(url)
    if text.startswith("Error"):
        return f"❌ Failed to fetch transcript: {text}"
    chunks = store_transcript(text)
    return f"✅ Video loaded successfully! {chunks} chunks stored and ready for questions."

tools = [
    Tool(
        name="YouTube_Loader",
        func=load_and_store_video,
        description=(
            "Load a YouTube video and store its transcript for Q&A. "
            "Input must be a full YouTube URL like  https://youtu.be/7NMYz-kRtdM . "
            "Always use this tool first before answering questions about a video."
        )
    ),
    Tool(
        name="Transcript_Search",
        func=search_transcript,
        description=(
            "Search the loaded YouTube transcript to answer questions. "
            "Input is a natural language question. "
            "Only use this after YouTube_Loader has been called."
        )
    ),
    Tool(
        name="Web_Search",
        func=web_search,
        description="Search the web for additional information. Input is a search query."
    ),
]


prompt=hub.pull("hwchase17/react")
agent=create_react_agent(llm=llm,tools=tools,prompt=prompt)
agent_executor=AgentExecutor(
agent=agent,
tools=tools,
verbose=True,
max_iterations=5,
handle_parsing_errors=True
)

def chat(question):
    response=agent_executor.invoke({"input":question})
    return response['output']