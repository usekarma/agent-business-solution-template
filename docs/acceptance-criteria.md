# Acceptance Criteria

Replace these examples with executable project criteria.

## Functional

- [ ] Given a valid request, the system produces the expected business result.
- [ ] Invalid input is rejected with a clear error and no partial side effect.
- [ ] Duplicate processing does not create duplicate business side effects.

## Reliability

- [ ] External calls have explicit timeouts.
- [ ] Transient failures are retried only when safe.
- [ ] Permanent failures are surfaced and diagnosable.

## Observability

- [ ] Important operations emit structured logs.
- [ ] A stable request/correlation identifier can trace one operation end-to-end.
- [ ] Failure state is visible without inspecting source code.

## Security

- [ ] No secrets are committed to the repository.
- [ ] Inputs are validated at trust boundaries.
- [ ] Permissions follow least privilege.

## Performance

- [ ] Define expected workload and acceptable latency/resource usage.
