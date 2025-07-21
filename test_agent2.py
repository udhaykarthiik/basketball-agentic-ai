from agents.pattern_finder_agent import pattern_finder_agent

sample_logs = """
Game 1: Q2, #12, #7, Success rate: 50%, Initiated by turnovers.
Game 2: Q3, #12, Success rate: 75%, Initiated by defensive rebounds.
Game 3: Q1, #7, Success rate: 60%, Initiated by steals.
Game 4: Q4, #12, #5, Success rate: 40%, Initiated by turnovers.
Game 5: Q2, #7, #11, Success rate: 80%, Initiated by defensive rebounds.
Game 6: Q1, #12, Success rate: 65%, Initiated by steals.
Game 7: Q3, #7, #12, Success rate: 55%, Initiated by turnovers.
"""

output = pattern_finder_agent(sample_logs)
print("\n=== Agent Output ===")
print(output)
