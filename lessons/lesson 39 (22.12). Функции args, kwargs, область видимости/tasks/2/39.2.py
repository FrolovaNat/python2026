def prepare_request(**kwargs):
    endpoint = kwargs.get("endpoint", "endpoint is required")
    control = {'timeout': 5, 'retries': 3}
    payload = kwargs.get("data")

    extras = {key: value for key, value in kwargs.items() if key in prepare_request}
    return {
        "endpoint": endpoint,
        "control": control,
        "payload": data,
    }


print(prepare_request(endpoint="/stats", data=[1, 2]))
print(prepare_request(endpoint="/sync", timeout=10, retries=0, mode="fast"))
