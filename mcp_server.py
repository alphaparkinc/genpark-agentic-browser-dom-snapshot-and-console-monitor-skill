"""MCP server for Browser DOM Snapshot Monitor."""
import sys
import json
from client import BrowserDOMSnapshotMonitor

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "inspect_browser_state",
                "description": "Extracts interactive DOM controls and filters critical console warnings",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "raw_html": {"type": "string"},
                        "console_logs": {"type": "array"}
                    },
                    "required": ["raw_html", "console_logs"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "inspect_browser_state":
            args = params.get("arguments", {})
            res = BrowserDOMSnapshotMonitor.process_browser_state(
                args.get("raw_html", ""),
                args.get("console_logs", [])
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
