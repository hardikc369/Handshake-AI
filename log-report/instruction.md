There is an Apache-style access log at `/app/access.log`. Parse it and write a
JSON summary report to `/app/report.json`.

The report must be a JSON object with exactly these three fields:

- `total_requests` (integer): the total number of log lines in the file.
- `unique_ips` (integer): the number of distinct client IP addresses that appear.
- `top_path` (string): the request path (e.g. `/index.html`) that appears most
  often across all requests. If there is a tie, use whichever of the tied
  paths appears first in the log.

Success criteria:
1. `/app/report.json` exists and contains a valid JSON object.
2. `total_requests` matches the actual number of log lines.
3. `unique_ips` matches the actual number of distinct client IPs.
4. `top_path` matches the actual most-frequent request path.
