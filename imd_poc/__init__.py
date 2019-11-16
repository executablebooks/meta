# monkey-patch panflute, include rst in raw formats
# TODO this should be fixed upstream
try:
    import panflute

    panflute.elements.RAW_FORMATS = {
        "html",
        "tex",
        "latex",
        "context",
        "rtf",
        "opendocument",
        "noteref",
        "openxml",
        "icml",
        "markdown",
        "mediawiki",
        "rst",
    }
except ImportError:
    pass
