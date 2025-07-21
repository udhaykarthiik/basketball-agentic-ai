from agents.data_collector_agent import data_collector_agent

sample_data = """
Lakers won the game 102-95 against the Heat. LeBron scored 27 points, 3 of which were 3-pointers.
There were 15 fast break points in total by the Lakers.
"""

output = data_collector_agent(sample_data)

print("\n=== Agent Output ===")
print(output)
