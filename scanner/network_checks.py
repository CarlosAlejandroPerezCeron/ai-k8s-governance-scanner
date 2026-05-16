from kubernetes import client, config

def check_missing_network_policies():
    config.load_kube_config()
    net_api = client.NetworkingV1Api()
    policies = net_api.list_network_policy_for_all_namespaces()

    if not policies.items:
        return ["No NetworkPolicy defined in cluster"]

    return []
