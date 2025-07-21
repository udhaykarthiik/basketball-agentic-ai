from agents.pattern_improvement_agent import pattern_improvement_agent

sample_logs = """
Game 1:
Player #7 - Points: 18, Rebounds: 5
Player #12 - Points: 15, Rebounds: 10

Game 2:
Player #7 - Points: 14, Rebounds: 4
Player #12 - Points: 17, Rebounds: 11
"""

print("=== Agent 4 Output ===")
output = pattern_improvement_agent(sample_logs)
print(output)
