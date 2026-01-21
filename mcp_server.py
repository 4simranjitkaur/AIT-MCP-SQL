from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("Postgres MCP Server")

API_BASE = "http://127.0.0.1:8000"


@mcp.tool()
def create_user(name: str, email: str):
    """Create a new user in the database"""
    response = httpx.post(
        f"{API_BASE}/users",
        params={"name": name, "email": email}
    )
    return response.json()


@mcp.tool()
def get_users():
    """Fetch all users from the database"""
    response = httpx.get(f"{API_BASE}/users")
    return response.json()
