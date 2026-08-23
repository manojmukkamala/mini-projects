# inko_random_wikipedia_article

Tiny CLI that fetches a **random English Wikipedia article** and prints
its title + summary, wrapped at 72 columns. Built as a uv-managed
package: `httpx` (HTTP/2) for the request, `rich` for rendering, and a
polite `User-Agent` assembled from the package's own metadata
(`inko-random-wikipedia-article/0.1 (Contact: info@user.com)`) — a
small exercise in metadata-driven, well-behaved clients.

The original zero-dependency iteration (stdlib `urllib` + `textwrap`)
is preserved, commented out, at the top of
`inko_random_wikipedia_article.py`.

## Files

- `inko_random_wikipedia_article.py` — the program (single module).
- `pyproject.toml` — PEP 621 manifest, hatchling build, console script
  `inko-random-wikipedia-article`, dev group `pytest`.
- `uv.lock` — committed lockfile (pins as of May 2025).
- `tests/` — one test: the User-Agent builder includes the package
  name and a contact.

## How to run

```sh
uv sync          # creates .venv, installs deps from uv.lock
uv run inko-random-wikipedia-article   # the console entry point
uv run pytest    # the test suite (1 test)
```

Each run prints a different article (the API picks at random).

## Data

No datasets. Live API, public, no key required:

```
https://en.wikipedia.org/api/rest_v1/page/random/summary
```
