# import os
# import time
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.agents import initialize_agent, AgentType
# from langchain_community.tools import DuckDuckGoSearchRun  # dummy tool

# load_dotenv()

# def pattern_finder_agent(game_logs_text):
#     time.sleep(2)

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-2.0-flash",
#         temperature=0.3,
#         google_api_key=os.getenv("GEMINI_API_KEY_PATTERN"),
#         convert_system_message_to_human=True
#     )

#     # Dummy search tool to satisfy agent requirement (won't actually be used)
#     search_tool = DuckDuckGoSearchRun()
#     tools = [search_tool]

#     agent = initialize_agent(
#         tools=tools,
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         verbose=True,
#         handle_parsing_errors=True  # prevents crash on LLM output formatting issues
#     )

#     prompt = f"""
# You are a basketball analytics expert.

# Analyze the following 7 night basketball game logs of Team X and identify patterns related to fast break plays:

# - When do fast breaks mostly occur? (Start, mid, or end of quarters?)
# - Which players are involved repeatedly?
# - How does Team X initiate fast breaks?
# - Any pattern in their success or failure?

# Game Logs:
# {game_logs_text}

# Output in structured points.
# """

#     return agent.run(prompt)






import os
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
# from langchain.agents.agent_toolkits import Tool  # for dummy tool

load_dotenv()

def pattern_finder_agent(game_logs_text):
    time.sleep(2)

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.3,
        google_api_key=os.getenv("GEMINI_API_KEY_PATTERN"),
        convert_system_message_to_human=True
    )

    # Dummy tool just to satisfy LangChain's structure
    dummy_tool = Tool(
        name="NoTool",
        func=lambda x: "This tool does nothing.",
        description="Placeholder tool for agent compliance."
    )

    agent = initialize_agent(
        tools=[dummy_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

    prompt = f"""
You are a basketball analytics expert.

Analyze the following 7-night basketball game logs of Team X to identify fast break play patterns:

1. When do fast breaks mostly occur? (Start, mid, or end of quarters?)
2. Which players are repeatedly involved?
3. How does Team X usually initiate fast breaks?
4. Any success/failure patterns?

Game Logs:
{game_logs_text}

Respond with a bullet-point analysis under clear headers:
- Fast Break Timing:
- Key Players Involved:
- Initiation Methods:
- Success/Failure Patterns:
"""

    return agent.run(prompt)
