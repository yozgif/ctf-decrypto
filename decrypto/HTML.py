import html


def en(s):
    return html.escape(s)

def de(s):
    return html.unescape(s)
