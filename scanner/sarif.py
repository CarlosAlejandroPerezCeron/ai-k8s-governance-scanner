import json

def generate_sarif(results):
    sarif = {
        "version": "2.1.0",
        "runs": [{
            "tool": {"driver": {"name": "AI Governance Scanner"}},
            "results": []
        }]
    }

    for r in results:
        for finding in r["findings"]:
            sarif["runs"][0]["results"].append({
                "message": {"text": finding},
                "level": "error"
            })

    return json.dumps(sarif, indent=2)
