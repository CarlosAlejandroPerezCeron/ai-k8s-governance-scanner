def check_image_digest(container):
    findings = []
    image = container.get("image", "")

    if "@sha256:" not in image:
        findings.append("Image not pinned by digest")

    if ":latest" in image:
        findings.append("Image uses latest tag")

    return findings


def check_security_context(container):
    findings = []
    ctx = container.get("securityContext", {})

    if not ctx.get("runAsNonRoot"):
        findings.append("runAsNonRoot not set")

    if not ctx.get("readOnlyRootFilesystem"):
        findings.append("readOnlyRootFilesystem not enabled")

    return findings