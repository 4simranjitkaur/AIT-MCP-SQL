FORBIDDEN_KEYWORDS = [
    "insert", "update", "delete", "drop",
    "alter", "truncate", "create"
]

def validate_query(sql: str):
    lowered = sql.lower()
    for word in FORBIDDEN_KEYWORDS:
        if word in lowered:
            raise ValueError("Blocked by MCP: Read-only queries only")
    return True
