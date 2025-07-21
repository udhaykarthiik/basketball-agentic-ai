# import os
# import time
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.agent_toolkits.load_tools import load_tools
# from langchain.agents import initialize_agent, AgentType

# load_dotenv()

# def data_collector_agent(game_text_data):
#     time.sleep(2)  # Pause to avoid hitting rate limits or to simulate delay

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-1.5-flash",
#         temperature=0.2,
#         google_api_key=os.getenv("GEMINI_API_KEY"),
#         convert_system_message_to_human=True
#     )

#     # Dummy tool just to satisfy LangChain's agent structure
#     tools = load_tools(["wikipedia"], llm=llm)

#     agent = initialize_agent(
#         tools=tools,
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         verbose=True,
#         handle_parsing_errors=True
#     )

#     prompt = f"""
# From the following basketball game text, extract the structured insights:

# 1. Which team won the game?
# 2. Total fast break points
# 3. Total 3-pointers
# 4. Final score summary

# Game Text:
# {game_text_data}

# Respond in structured format.
# """

#     return agent.run(prompt)





import os
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# from langchain.agents.agent_toolkits import Tool

load_dotenv()

def data_collector_agent(game_text_data):
    time.sleep(2)  # Avoid rapid calls

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.2,
        google_api_key=os.getenv("GEMINI_API_KEY"),
        convert_system_message_to_human=True
    )

    # Dummy tool to allow LangChain agent to work
    dummy_tool = Tool(
        name="NoTool",
        func=lambda x: "This tool is a placeholder.",
        description="This tool does nothing and only exists to let the agent run."
    )

    agent = initialize_agent(
        tools=[dummy_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

    prompt = f"""
You are a basketball data analyzer.

From the game log text below, extract the following details in this format:

Team Won: <Team Name or Unknown>
Fast Break Points: <Number or Unknown>
Total 3-Pointers: <Number or Unknown>
Final Score Summary: <Text Summary>

Game Log:
{game_text_data}
"""

    return agent.run(prompt)
