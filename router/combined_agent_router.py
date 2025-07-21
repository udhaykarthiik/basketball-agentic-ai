# combined_agent_router.py
import time
from agents.data_collector_agent import data_collector_agent
from agents.pattern_analyzer_agent import pattern_analyzer_agent
from agents.pattern_finder_agent import pattern_finder_agent
from agents.pattern_improvement_agent import pattern_improvement_agent
from agents.team_strategy_agent import team_strategy_agent

def run_all_agents(logs):
    data_collector_output = data_collector_agent(logs)
    pattern_analyzer_output = pattern_analyzer_agent(logs)
    pattern_finder_output = pattern_finder_agent(logs)
    pattern_improvement_output = pattern_improvement_agent(logs)
    team_strategy_output = team_strategy_agent(logs)

    combined_output = (
        f"\n\n📥 Data Collector Agent:\n{data_collector_output}\n\n"
        f"🔍 Pattern Analyzer Agent:\n{pattern_analyzer_output}\n\n"
        f"📈 Pattern Finder Agent:\n{pattern_finder_output}\n\n"
        f"⚙️ Pattern Improvement Agent:\n{pattern_improvement_output}\n\n"
        f"🎯 Team Strategy Agent:\n{team_strategy_output}"
    )

    return {
        "combined": combined_output,
        "data_collector": data_collector_output,
        "pattern_analyzer": pattern_analyzer_output,
        "pattern_finder": pattern_finder_output,
        "pattern_improvement": pattern_improvement_output,
        "team_strategy": team_strategy_output,
    }
