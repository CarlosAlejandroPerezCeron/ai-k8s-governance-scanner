from .checks_security import check_image_digest, check_security_context
from .checks_cost import check_resources
from .scoring import calculate_risk

def analyze_workload(doc):
    kind = doc.get("kind")
    metadata = doc.get("metadata", {})
    name = metadata.get("name", "unknown")

    findings = []

    if kind in ["Deployment", "StatefulSet", "DaemonSet"]:
        containers = doc["spec"]["template"]["spec"]["containers"]

        for container in containers:
            findings.extend(check_image_digest(container))
            findings.extend(check_security_context(container))
            findings.extend(check_resources(container))

    risk = calculate_risk(findings)

    return {
        "name": name,
        "kind": kind,
        "findings": findings,
        "risk": risk
    }