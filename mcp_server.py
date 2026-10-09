from fastmcp import FastMCP # import FastMcp Class
import subprocess

mcp = FastMCP("Docker Mcp Server") # mcp obeject of class
@mcp.tool
def show_all_containers():
    """Show all currently running Docker containers."""
    
    result = subprocess.run(
        ["docker", "ps","-a"],
        capture_output=True,
        text=True,
        check=False
    )

    return result.stdout

@mcp.tool
def show_running_containers():
    """Show all currently running Docker containers."""
    
    result = subprocess.run(
        ["docker", "ps"],
        capture_output=True,
        text=True,
        check=False
    )

    return result.stdout

if __name__ == "__main__" :
    mcp.run()
