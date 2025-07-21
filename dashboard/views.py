# from django.shortcuts import render
# from router.combined_agent_router import run_all_agents

# def analyze_logs(request):
#     if request.method == "POST":
#         logs = request.POST.get("logs")
#         if logs:
#             result_dict = run_all_agents(logs)
#         else:
#             result_dict = {"combined": "No logs provided."}
#         return render(request, "analyze.html", {"results": result_dict, "logs": logs})
#     return render(request, "analyze.html")

from django.shortcuts import render
from router.combined_agent_router import run_all_agents

def analyze_logs(request):
    results = None
    logs = ""
    
    if request.method == "POST":
        logs = request.POST.get("logs", "")
        if logs.strip():
            results = run_all_agents(logs)
        else:
            results = {
                "combined": "⚠️ No logs provided.",
                "data_collector": "",
                "pattern_analyzer": "",
                "pattern_finder": "",
                "pattern_improvement": "",
                "team_strategy": ""
            }

    return render(request, "analyze.html", {"results": results, "logs": logs})
