# AI Kubernetes Governance Scanner v1.0.0

Status: Active Development  
Maturity: Functional CLI Tool  

---

## Executive Summary

AI workloads running on Kubernetes introduce elevated operational and financial risk.

Common failures include:

- Unbounded GPU consumption
- Missing resource limits
- Insecure container configurations
- Use of mutable image tags
- Absence of runtime security controls

This tool provides automated governance scanning for AI workloads deployed in Kubernetes.

It analyzes workload manifests and produces structured risk assessments.

---

## What This Tool Detects

Security Checks:
- Image not pinned by digest
- Usage of :latest tag
- Missing runAsNonRoot
- Missing readOnlyRootFilesystem

Cost & Resource Checks:
- Missing resource limits
- Missing resource requests
- GPU declared incorrectly
- Unbounded container resource allocation

Risk Scoring:
- CLEAN
- LOW
- MEDIUM
- HIGH
- CRITICAL

---

## Why This Matters

AI infrastructure failures are rarely model failures.
They are governance failures.

This scanner identifies:

- Financial exposure
- Security misconfigurations
- Operational instability risks

before deployment.

---

## Installation

Clone repository:
