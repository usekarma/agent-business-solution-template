---
name: problem-to-solution
description: Convert a business problem into requirements, architecture, acceptance criteria, implementation slices, and verification steps.
---

# Problem to Solution

Use this workflow when the task begins as a business problem rather than a precise code change.

## Workflow

1. Read `PROJECT_BRIEF.md` and existing acceptance criteria.
2. Identify the business outcome and measurable success condition.
3. Inspect the existing repository for reusable components and constraints.
4. Separate requirements into:
   - functional behavior
   - reliability
   - security
   - performance
   - observability
5. Identify ambiguity. Make explicit, conservative assumptions when work can proceed safely.
6. Propose the smallest architecture that satisfies the requirements.
7. Identify data ownership, trust boundaries, failure boundaries, and idempotency boundaries.
8. Define executable acceptance tests before large implementation work.
9. Implement in vertical slices that produce demonstrable behavior.
10. Run project checks and perform an independent production review.

## Avoid

- starting from a preferred cloud service instead of the business problem
- inventing distributed components without a concrete need
- generating large amounts of code before defining acceptance behavior
- treating a passing happy-path test as production readiness
