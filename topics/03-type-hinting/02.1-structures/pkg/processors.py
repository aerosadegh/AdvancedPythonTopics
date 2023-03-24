# multiple options


def process(response):
    if response is None:
        return None
    if isinstance(response, int):
        return response, str(response)
    
    if isinstance(response, bytes):
        return response.decode("utf-8")

