from agents.pattern_analyzer_agent import pattern_analyzer_agent

sample_logs = """
Game 1 - Player #7: 22 pts, Player #12: 18 pts, Player #5: 9 pts
Game 2 - Player #7: 10 pts, Player #12: 20 pts
Game 3 - Player #7: 15 pts, Player #12: 14 pts
Game 4 - Player #7: 25 pts, Player #12: 17 pts
"""

output = pattern_analyzer_agent(sample_logs)
print("\n=== Agent Output ===")
print(output)
