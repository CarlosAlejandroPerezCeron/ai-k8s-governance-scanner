from kubernetes import client, config

def check_cluster_admin_bindings():
    config.load_kube_config()
    rbac = client.RbacAuthorizationV1Api()
    bindings = rbac.list_cluster_role_binding()

    risky = []
    for b in bindings.items:
        if b.role_ref.name == "cluster-admin":
            risky.append(f"Cluster-admin binding found: {b.metadata.name}")

    return risky
