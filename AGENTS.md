# AGENTS.md

Guidance for AI agents (and humans) working in this repo.

## What this repo is
A collection of small personal projects, experiments, and coursework —
mostly Python, plus some R, SQL, and MATLAB. Projects are fully
standalone; nothing depends on anything else at the top level.

## Naming
- One top-level folder per project, named `snake_case`
  (e.g. `text_analytics`). No spaces, no CamelCase.
- Python files: `snake_case`, PEP 8.
- Every project should have a short `README.md`:
  what it is and how to run it.

## Python environments
- **One `.venv` per project, created on demand.** Never a shared env —
  projects pin conflicting versions across eras.
- **Dependency standard: `pyproject.toml` + `uv.lock` per project.**
  - `pyproject.toml` declares dependencies (PEP 621 `[project]` table).
  - `uv.lock` is the committed lockfile — reproducible installs.
  - Workflow: `cd <project> && uv sync` (creates `.venv`, installs from lock).
  - Legacy `requirements.txt` files are migrated when a project is next
    touched: convert deps into `[project] dependencies`, then `uv lock`.
- `pyproject.toml` and `uv.lock` are **committed**; `.venv/` is gitignored.
- Don't change dependency pins in a project you aren't actively running
  (a fresh `uv lock` may bump versions — that's fine, note it in the commit).

## Keeping the repo slim
- Target: repo stays well under ~100 MB.
- No videos, no `.mat`/`.h5` datasets, no model weights, no large CSVs
  in git. Course datasets and weights are re-downloaded on demand;
  document the source URL in the project README.
- `.DS_Store`, `__pycache__/`, `*.pyc`, `.ipynb_checkpoints/` are
  gitignored — never commit them.
- Prefer clearing notebook outputs before committing.

## House rules
- Personal repo: work on `main` directly by default; use branches
  when a change is big or experimental.
- Never delete a project folder without explicit confirmation.
