# Project agent instructions

## Mission

Solve the business problem described in `PROJECT_BRIEF.md` with the smallest production-worthy design that satisfies `docs/acceptance-criteria.md`.

Do not optimize for amount of code. Optimize for correct behavior, clarity, operability, and ease of change.

## Required workflow

Before changing code:

1. Read `PROJECT_BRIEF.md`.
2. Read `docs/acceptance-criteria.md`.
3. Inspect relevant existing code and tests.
4. State material assumptions.
5. Prefer the smallest coherent vertical slice.

After changing code:

1. Add or update tests for behavior changes.
2. Run `./scripts/check.sh` when available.
3. Review the diff for unintended changes.
4. Confirm each affected acceptance criterion.
5. Report unresolved risks or assumptions.

## Architecture rules

- Keep domain/business logic independent from frameworks and cloud SDKs.
- Put external I/O behind small interfaces/ports.
- Prefer dependency injection over hidden globals.
- Keep functions and classes small enough to test independently.
- Reuse existing project patterns before introducing new abstractions.
- Do not create an abstraction until it reduces real duplication or isolates a real dependency.

## Reliability rules

For external or distributed operations:

- Use explicit timeouts.
- Make retry behavior deliberate and bounded.
- Consider idempotency before enabling retries.
- Do not silently swallow exceptions.
- Make partial failure observable.
- Prefer structured logs with stable identifiers/correlation IDs.
- Document recovery behavior for operations that can partially complete.

## Security rules

- Never commit secrets, credentials, tokens, private keys, or real customer data.
- Prefer least-privilege permissions.
- Treat input from APIs, files, queues, and users as untrusted.
- Never execute destructive cloud or production commands unless the human explicitly authorizes that exact action.
- Specifically do not run `terraform apply`, `terraform destroy`, delete commands, production database writes, or irreversible migrations without explicit human approval.

## Testing rules

Tests should prove behavior, not implementation details.

Cover when relevant:

- success path
- invalid input
- boundary conditions
- external failure
- timeout/retry behavior
- duplicate/idempotent processing
- partial failure
- authorization/security boundary

Do not weaken or delete a failing test merely to make the build green unless the requirement itself changed and the reason is documented.

## Python rules

- Python 3.12+
- Type hints on public functions/methods
- `pytest` for tests
- `ruff` for linting
- `mypy` for type checks
- Prefer standard library unless a dependency materially improves the solution

## Infrastructure rules

- Infrastructure belongs in `infra/` and should be managed as code.
- Keep application configuration separate from secrets.
- Any destructive infrastructure action requires human authorization.

## Definition of done

A task is done only when:

- behavior is implemented
- relevant automated tests pass
- lint/type checks pass
- acceptance criteria are addressed
- production failure/recovery implications are understood
- the final diff has been reviewed
