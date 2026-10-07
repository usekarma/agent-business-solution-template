# Agent Business Solution Template

A practical starter repository for using VS Code coding agents to turn a business problem into a tested, reviewable software solution.

## What this template optimizes for

- Business requirements before implementation
- Small, reviewable changes
- Executable acceptance criteria
- Agent-friendly commands
- Clear architecture boundaries
- Production-minded testing and review
- Safe defaults around cloud/infrastructure actions

## Start a new project

1. Copy this repository.
2. Replace the placeholders in `PROJECT_BRIEF.md`.
3. Fill in `docs/acceptance-criteria.md`.
4. Open the repository root in VS Code.
5. Start with the **Architect** agent and ask:

   > Read `PROJECT_BRIEF.md`, `AGENTS.md`, and the existing repository. Produce the smallest coherent implementation plan that satisfies the acceptance criteria. Do not code yet.

6. Switch to **Builder** when the plan is sound.
7. Run `./scripts/check.sh` before considering the task complete.
8. Use **Reviewer** and **Operations** as independent second opinions.

## Repository layout

```text
.
├── AGENTS.md
├── PROJECT_BRIEF.md
├── .github/
│   ├── agents/
│   │   ├── architect.agent.md
│   │   ├── builder.agent.md
│   │   ├── operations.agent.md
│   │   └── reviewer.agent.md
│   ├── instructions/
│   │   └── python.instructions.md
│   ├── skills/
│   │   ├── problem-to-solution/SKILL.md
│   │   └── production-review/SKILL.md
│   └── hooks/
│       ├── README.md
│       └── audit.json.example
├── docs/
│   ├── acceptance-criteria.md
│   ├── architecture.md
│   ├── decision-log.md
│   └── runbook.md
├── src/business_app/
├── tests/
├── scripts/
└── infra/
```

## Local setup

Requires Python 3.12+.

```bash
./scripts/bootstrap.sh
source .venv/bin/activate
./scripts/check.sh
```

On Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest
python -m ruff check .
python -m mypy src
```

## Agent workflow

### 1. Architect

Ask the agent to understand the business outcome, inspect the repository, identify ambiguity, choose boundaries, and propose acceptance tests.

### 2. Builder

Ask the agent to implement one vertical slice at a time and continuously run the test/check commands.

### 3. Reviewer

Ask for a hostile review of the diff: correctness, race conditions, retries, security, resource usage, error handling, and weak tests.

### 4. Operations

Ask how the system fails in production, how you will know, how you recover, and what should be in the runbook.

## Important safety rule

The repository instructions prohibit destructive production/cloud actions unless the human explicitly authorizes them. Keep that rule even when you customize this template.

## VS Code agent customization

VS Code discovers workspace custom agents from `.github/agents` and project skills from `.github/skills`. `AGENTS.md` is a cross-agent project instruction format supported by VS Code/Copilot and OpenAI Codex-compatible workflows.

Hooks differ by harness. An example is included but intentionally disabled as `audit.json.example`; read `.github/hooks/README.md` before enabling it.
