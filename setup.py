from setuptools import setup, find_packages

setup(
    name="ai-k8s-governance-scanner",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "click"
    ],
    entry_points={
        "console_scripts": [
            "ai-scan=cli:scan"
        ]
    }
)
