
def wire(container, mapping):
    for name, service in mapping.items():
        container.add(name, service)
    return container
