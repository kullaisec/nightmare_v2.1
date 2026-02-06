def parse_body(raw, length):
    """
    Simulates backend HTTP body parsing
    using Content-Length
    """
    if length is None:
        return raw
    return raw[:length]