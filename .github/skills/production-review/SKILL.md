---
name: production-review
description: Stress-test an implementation for production correctness, failure handling, operability, and safe recovery.
---

# Production Review

Evaluate the implementation under adverse conditions.

For each external boundary, ask:

- What if it is slow?
- What if it returns an error?
- What if the response is received but acknowledgment is lost?
- What if the caller retries?
- What if two workers process the same logical operation?
- What if the process crashes after the external side effect but before local state is updated?

Also inspect:

- unbounded collections or payloads
- concurrency limits and backpressure
- missing timeouts
- unsafe retry loops
- inadequate identifiers/correlation
- secrets in code/logs
- overbroad permissions
- insufficient metrics/alerts
- inability to replay or repair safely

For every serious issue, propose a regression test or executable check.
