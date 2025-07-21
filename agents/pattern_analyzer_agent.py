# import os
# import time
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.agent_toolkits.load_tools import load_tools
# from langchain.agents import initialize_agent, AgentType

# load_dotenv()

# def pattern_analyzer_agent(player_logs_text):
#     time.sleep(2)

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-1.5-flash",
#         temperature=0.2,
#         google_api_key=os.getenv("GEMINI_API_KEY_AGENT3"),
#         convert_system_message_to_human=True,
#         handle_parsing_errors=True
#     )

#     # Dummy tool to avoid ZeroShotAgent error
#     tools = load_tools(["wikipedia"], llm=llm)

#     # Initialize agent with parsing error handler
#     agent = initialize_agent(
#         tools=tools,
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         verbose=True,
#         handle_parsing_errors=True  # ✅ important fix
#     )

#     prompt = f"""
# You are a basketball performance analyst.

# Analyze the following player performance logs and find meaningful patterns.

# Please answer in this format:
# Thought: [Your thought]
# Action: [use Tool if needed or say 'None']
# Action Input: [only if tool is used]
# Observation: [optional]
# Final Answer: [structured format]

# Logs:
# {player_logs_text}
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

def pattern_analyzer_agent(player_logs_text):
    time.sleep(2)

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.2,
        google_api_key=os.getenv("GEMINI_API_KEY_AGENT3"),
        convert_system_message_to_human=True
    )

    # Dummy tool to satisfy agent requirements
    dummy_tool = Tool(
        name="NoTool",
        func=lambda x: "This tool does nothing.",
        description="This is a placeholder tool."
    )

    agent = initialize_agent(
        tools=[dummy_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

    prompt = f"""
You're a basketball analyst.

Analyze the following player logs and identify key performance patterns:
1. Are there any trends in scoring, assists, or rebounds?
2. Any standout players or underperformers?
3. Are there consistency issues across games?

Respond in this format:
- Key Trends:
- Standout Players:
- Underperformers:
- Consistency Notes:

Logs:
{player_logs_text}
"""

    return agent.run(prompt)
