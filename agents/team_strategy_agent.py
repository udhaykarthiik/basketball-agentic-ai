# import os
# from dotenv import load_dotenv
# import time
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.agent_toolkits.load_tools import load_tools
# from langchain.agents import initialize_agent, AgentType

# load_dotenv()

# def team_strategy_agent(team_logs_text):
#     time.sleep(1)

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-1.5-flash",
#         temperature=0.3,
#         google_api_key=os.getenv("GEMINI_API_KEY_AGENT5")
#     )

#     # Load dummy tool just to satisfy the agent (won’t really use it)
#     tools = load_tools(["wikipedia"], llm=llm)

#     agent = initialize_agent(
#         tools=tools,
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         verbose=True,
#         handle_parsing_errors=True
#     )

#     prompt = f"""
# You are a tactical strategist for a professional basketball team.

# Analyze the following **team performance logs across 3 games** and provide your expert insights.

# Focus on:
# - Offensive vs defensive consistency
# - Game tempo or pace
# - Any strategic flaws (e.g. slow starts, 4th quarter drops)
# - Overall coaching impact
# - Suggestions for improvement

# Game Logs:
# {team_logs_text}

# Respond with a professional tone and structured format.
# """

#     return agent.run(prompt)






import os
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import Tool
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent, AgentType

load_dotenv()

def team_strategy_agent(team_logs_text):
    time.sleep(1)  # Prevent rate limit issues

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.3,
        google_api_key=os.getenv("GEMINI_API_KEY_AGENT5"),
        convert_system_message_to_human=True  # Helps avoid parser format issues
    )

    # Use dummy tools to satisfy LangChain agent interface
    tools = load_tools(["wikipedia"], llm=llm)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True  # ✅ Prevents crashing on format mismatch
    )

    prompt = f"""
You are a tactical strategist for a professional basketball team.

Analyze the following **team performance logs across 3 games** and provide your expert insights.

**Instructions:**
- Evaluate offensive vs defensive consistency
- Comment on game tempo or pace
- Identify any strategic flaws (e.g., slow starts, 4th quarter drop-offs)
- Assess overall coaching impact
- Provide actionable suggestions for improvement

Game Logs:
{team_logs_text}

**Format your response like this:**
Thought: [your reasoning]
Action: None
Final Answer:
- Offensive/Defensive Notes:
- Tempo/Pace Insights:
- Flaws Observed:
- Coaching Impact:
- Suggestions:
"""

    return agent.run(prompt)


