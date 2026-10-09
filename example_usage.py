"""Example usage for Browser DOM Snapshot Monitor."""
from client import BrowserDOMSnapshotMonitor

if __name__ == "__main__":
    html = "<html><body><button id='login'>Sign In</button><input type='password'/></body></html>"
    logs = [{"level": "info", "message": "DOM ready"}]
    state = BrowserDOMSnapshotMonitor.process_browser_state(html, logs)
    print("Page State:", state["page_state"])
    print("Interactive Elements:", state["interactive_elements_count"])
