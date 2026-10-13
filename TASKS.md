# Work inbox (optional)

Capture small requests here without interrupting the primary project. An entry is **not** permission to start work, launch an agent, change cloud resources, or merge a PR. Use GitHub Issues instead if the list becomes difficult to maintain.

## How to use

1. Add ideas and requests under **Inbox** as they arise. No branch is needed to record a task.
2. Move a clearly scoped task to **Ready** when its outcome, owner, dependencies, and affected files or systems are understood.
3. Move a task to **In progress** only when execution has actually started. **As a starting guideline, work on no more than two independent tasks at once**, and fewer when work overlaps. This is a *manual preference*, not an automated scheduler or an enforced guarantee.
4. If tasks touch the same files, contracts, AWS resources, credentials, or architectural decisions, sequence them or explicitly coordinate before proceeding. Separate Git branches do not isolate shared infrastructure.
5. Move tasks to **Review / blocked** when waiting for evidence, a dependency, or a human decision. Mark **Done** only after the stated outcome has been verified.
6. Changes go through the existing specification, tests, security checks, pull request review, and authorization process. Infrastructure apply/destroy and other consequential actions always require explicit human approval.

For each task, record at minimum: **what**, **priority**, **owner**, **dependencies**, and **affected area**. Rough estimates are optional. Faraday or other agents can suggest prioritization, but should not silently change user priorities or start additional agents without instruction.

## Inbox

- [ ] Example: Investigate an open question — priority: low; owner: unassigned; depends on: none; affected area: research only.

## Ready

_None._

## In progress

_None._

## Review / blocked

_None._

## Done

_None._

## Not in scope

No automatic agent dispatch, background monitoring, CI concurrency gates, task scheduler, or additional infrastructure is introduced by this file.
