def parse_frontend(raw):
    if b"Transfer-Encoding: chunked" in raw:
        return raw.split(b"\r\n\r\n", 1)[1]
    return raw