"""Agentic Browser DOM Snapshot & Console Monitor.
100% Python Standard Library.
"""

import re

class BrowserDOMSnapshotMonitor:
    """Captures structured accessibility tree snapshots and intercepts runtime console logs."""
    
    @staticmethod
    def process_browser_state(raw_html: str, console_logs: list) -> dict:
        matches = re.findall(r"<(?:button|input|a|select)[^>]*>", raw_html, re.IGNORECASE)
        interactive_elements = [m[:100] for m in matches]
                
        critical_logs = [log for log in console_logs if log.get("level") in ["error", "warn"]]
        
        return {
            "interactive_elements_count": len(interactive_elements),
            "interactive_summary": interactive_elements[:10],
            "total_console_logs": len(console_logs),
            "critical_errors_count": len(critical_logs),
            "critical_logs": critical_logs,
            "page_state": "HEALTHY" if len(critical_logs) == 0 else "DEGRADED"
        }
