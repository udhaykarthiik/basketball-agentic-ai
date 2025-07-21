# import os
# import time
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# def pattern_improvement_agent(performance_logs_text):
#     time.sleep(1)

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-1.5-flash",
#         temperature=0.2,
#         google_api_key=os.getenv("GEMINI_API_KEY_AGENT4")
#     )

#     prompt = f"""
# You are a professional basketball performance analyst.

# Analyze the following player performance logs across two games and provide your insights.

# **Instructions:**
# 1. Identify who is improving.
# 2. Spot any decline in performance.
# 3. Mention any unusual patterns.
# 4. End with a clear summary.

# Game Logs:
# {performance_logs_text}
# """

#     result = llm.invoke(prompt)
#     return result.content






import os
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import Tool

load_dotenv()

def pattern_improvement_agent(performance_logs_text):
    time.sleep(1)  # Simulate natural delay or rate limit buffer

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.2,
        google_api_key=os.getenv("GEMINI_API_KEY_AGENT4"),
        convert_system_message_to_human=True  # Optional but helps prevent parsing issues
    )

    prompt = f"""
You are a professional basketball performance analyst.

Analyze the following player performance logs across two games and provide insights.

Respond in this format:
- Improving Players:
- Declining Players:
- Unusual Patterns:
- Summary:

Game Logs:
{performance_logs_text}
"""

    result = llm.invoke(prompt)
    return result.content.strip()

