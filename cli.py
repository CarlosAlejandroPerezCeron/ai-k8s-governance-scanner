import click
from scanner.loader import load_yaml_documents
from scanner.engine import analyze_workload
from scanner.reporter import generate_json_report, generate_markdown_report

@click.command()
@click.argument("file")
@click.option("--format", default="json", help="json or markdown")
def scan(file, format):
    docs = load_yaml_documents(file)
    results = []

    for doc in docs:
        if doc:
            results.append(analyze_workload(doc))

    if format == "json":
        print(generate_json_report(results))
    else:
        print(generate_markdown_report(results))

if __name__ == "__main__":
    scan()
