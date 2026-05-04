import yaml

def load_yaml_documents(file_path):
    with open(file_path, "r") as f:
        return list(yaml.safe_load_all(f))