import json

def generate_json_report(results):
    return json.dumps(results, indent=2)

def generate_markdown_report(results):
    md = "# AI Governance Report\n\n"
    for r in results:
        md += f"## {r['name']} ({r['kind']})\n"
        md += f"Risk Level: **{r['risk']}**\n\n"
        for f in r["findings"]:
            md += f"- {f}\n"
        md += "\n"
    return md