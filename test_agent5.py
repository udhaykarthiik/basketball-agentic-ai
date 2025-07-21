from agents.team_strategy_agent import team_strategy_agent

team_logs = """
Game 1:
Points Scored: 89 | Points Conceded: 76 | Turnovers: 12 | Rebounds: 44

Game 2:
Points Scored: 95 | Points Conceded: 91 | Turnovers: 17 | Rebounds: 39

Game 3:
Points Scored: 78 | Points Conceded: 88 | Turnovers: 14 | Rebounds: 37
"""

print("=== Agent 5 Output ===")
output = team_strategy_agent(team_logs)
print(output)
