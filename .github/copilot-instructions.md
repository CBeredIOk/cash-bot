# Copilot Code Review Instructions (Python Telegram finance bot)

## Context
Project: Telegram bot for personal finance tracking (expenses/income, reports).
Language: Python.

## Review priorities (highest → lowest)
1) **Simplicity (KISS)**
2) **Readability / maintainability**
3) **Security & privacy**
4) **Correctness / data integrity**
5) **Test coverage**
6) **Performance (only when it matters)**

If there is a trade-off, prefer **security + correctness + simplicity** over cleverness.

---

## General principles
- Keep It Stupid Simple: prefer straightforward solutions over “smart” abstractions.
- Prefer small, focused changes. Avoid broad refactors unless necessary.
- Avoid hidden side effects: functions should do what their name says.
- Prefer composition over inheritance.
- Prefer explicit over implicit; readability > micro-optimizations.

---

## Documentation & readability rules
- **Docstrings are required** for:
  - all public functions/classes/modules
  - any non-trivial private function (more than ~2 lines or non-obvious logic)
- Docstrings may be omitted only for **tiny helpers** (1–2 lines) that are self-explanatory.
- Docstrings should answer: *what it does*, *inputs/outputs*, *edge cases*, *raises* (if relevant).
- **Inline code comments must be in English** and used sparingly (only for non-obvious decisions).
- Prefer clear naming over comments. Avoid abbreviations unless domain-standard.

---

## Security checklist (must flag)
- **No secrets in code**: bot token, DB creds, API keys must come from environment/config.
- Do not log secrets or sensitive user data (PII). Redact where needed.
- Treat all Telegram input as **untrusted**:
  - validate and sanitize amounts, dates, categories, report parameters
  - handle unexpected formats gracefully
- If using SQL:
  - **parameterized queries only** (no string concatenation / f-strings in SQL)
  - validate identifiers if dynamic (table/column names) or avoid dynamic SQL altogether
- If using Markdown/HTML parse modes:
  - escape user-provided content to prevent formatting injection
- Avoid insecure randomness for tokens/IDs where security matters (use `secrets` module).
- Avoid unsafe deserialization (`pickle`, `eval`, `yaml.load` without safe loader, etc).

---

## Correctness & data integrity (finance domain)
- Money handling:
  - **Do not use float for money**.
  - Prefer `Decimal` with explicit quantization OR store amounts in **minor units (int)**.
  - Be explicit about rounding mode where applicable.
- Make operations idempotent where possible (Telegram retries / duplicate updates can happen).
- Validate constraints:
  - amounts must be positive where required, currency consistent, categories exist, dates parseable
- Time handling:
  - use timezone-aware datetimes; be explicit about user timezone vs server timezone
- Reports:
  - ensure ordering, grouping, and totals are deterministic and tested.

---

## Telegram bot specific concerns
- Error handling:
  - catch broad exceptions only at **handler boundaries**, log context safely, and return user-friendly messages
  - don’t swallow errors silently (`except Exception: pass`)
- Avoid blocking operations in async handlers:
  - DB/network/file I/O should be async or offloaded properly
- Rate limiting / spam resilience:
  - avoid expensive operations per message; consider caching where appropriate

---

## Code style expectations
- Follow PEP8 and project linters/formatters (e.g., ruff/black/isort) if configured.
- Prefer type hints for new/changed code, especially for public APIs and core logic.
- Keep functions small and testable:
  - parsing/validation/calculation should be separated from Telegram I/O glue
- Avoid unnecessary dependencies; prefer standard library when reasonable.

---

## Tests requirements
- New features or non-trivial bug fixes should include tests (pytest preferred).
- Focus tests on:
  - parsing user input (amount/date/category)
  - money arithmetic/rounding
  - report aggregation logic
  - DB repository methods (unit tests or lightweight integration where appropriate)
- Tests should be deterministic (no reliance on current time without freezing/mocking).

---

## Performance guidance
- Don’t optimize prematurely.
- Do flag obvious inefficiencies:
  - repeated DB queries in loops (N+1)
  - reading large datasets when aggregation can be done in DB
  - expensive formatting in hot paths
- Prefer simple optimizations with clear benefit (batching, indexing, caching).

---

## Review output format (how to comment)
When leaving review feedback:
- Be concrete: point to file/line/construct and explain the impact.
- If possible, propose a minimal fix or code suggestion.
- Label severity:
  - **BLOCKER**: security/correctness/data loss
  - **IMPORTANT**: maintainability/readability/test gaps
  - **NICE TO HAVE**: style/ergonomics/micro improvements

---

## Common “must-request-changes” examples
- floats used for money
- secrets committed
- SQL built via string concatenation
- missing docstrings for non-trivial functions/classes
- overly complex abstractions for simple tasks
- unhandled user input edge cases (crashes on unexpected message format)
- logging raw user data or tokens
