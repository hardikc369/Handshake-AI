import json
import re
from collections import Counter
from pathlib import Path


def _parse_log():
    """Ground truth, computed independently of the agent's code."""
    paths, ips, total = Counter(), set(), 0
    with open("/app/access.log") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            ips.add(line.split()[0])
            m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if m:
                paths[m.group(1)] += 1
    return {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0],
    }


def _load_report():
    return json.loads(Path("/app/report.json").read_text())


def test_criterion_1_report_exists_and_is_valid_json():
    """instruction.md criterion 1: /app/report.json exists and is a valid JSON object."""
    path = Path("/app/report.json")
    assert path.exists(), "no report.json found"
    data = json.loads(path.read_text())
    assert isinstance(data, dict), "report.json must contain a JSON object"


def test_criterion_2_total_requests_correct():
    """instruction.md criterion 2: total_requests matches the actual number of log lines."""
    expected = _parse_log()["total_requests"]
    actual = _load_report()["total_requests"]
    assert actual == expected, f"total_requests: expected {expected}, got {actual}"


def test_criterion_3_unique_ips_correct():
    """instruction.md criterion 3: unique_ips matches the actual number of distinct client IPs."""
    expected = _parse_log()["unique_ips"]
    actual = _load_report()["unique_ips"]
    assert actual == expected, f"unique_ips: expected {expected}, got {actual}"


def test_criterion_4_top_path_correct():
    """instruction.md criterion 4: top_path matches the actual most-frequent request path."""
    expected = _parse_log()["top_path"]
    actual = _load_report()["top_path"]
    assert actual == expected, f"top_path: expected {expected}, got {actual}"
