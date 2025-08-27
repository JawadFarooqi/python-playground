<div align="center">
	<h1>Python Playground</h1>
	<p><strong>A curated, progressive open-source path for beginners to learn Python with Jupyter notebooks.</strong></p>
	<p>
		<a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-GPLv3-blue.svg"></a>
		<a href=".github/workflows/ci.yml"><img alt="CI" src="https://github.com/JawadFarooqi/python-playground/actions/workflows/ci.yml/badge.svg"></a>
	</p>
</div>

## Why this project?

Most beginner resources mix too many ideas at once or hide important basics. This repository aims to provide:

- A clear sequential learning path
- Small, fast, reproducible notebooks
- Explicit learning objectives & exercises
- Clean code & modern tooling (Ruff, Black, Pytest)

## Quick Start

```bash
git clone https://github.com/JawadFarooqi/python-playground.git
cd python-playground
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install --upgrade pip
pip install .[dev]
pre-commit install
```

Open notebooks in your preferred environment (VS Code, JupyterLab) from the `notebooks/` directory.

## Repository Layout

```
src/playground/    # Reusable helper utilities imported by notebooks
notebooks/         # Learning tracks (to be populated)
tests/             # Pytest-based tests (unit + future notebook smoke tests)
docs/              # Documentation site sources
.github/           # CI workflows, issue templates, PR template
```

## Planned Notebook Tracks

| Track | Topic             | Focus                               |
| ----- | ----------------- | ----------------------------------- |
| 01    | Basics            | Syntax, variables, types, I/O       |
| 02    | Control Flow      | Conditionals, loops, comprehensions |
| 03    | Functions         | Defining, arguments, lambdas        |
| 04    | Data Structures   | Lists, tuples, dicts, sets          |
| 05    | OOP               | Classes, inheritance, dataclasses   |
| 06    | Modules & Env     | Imports, packaging, virtual envs    |
| 07    | Error Handling    | Exceptions, patterns                |
| 08    | IO & Files        | Files, JSON                         |
| 09    | Stdlib Essentials | datetime, pathlib, collections      |
| 10    | Testing           | Pytest basics                       |
| 11    | Tooling           | Linting, formatting, type hints     |
| 12    | Data Handling     | NumPy, pandas                       |
| 13    | Visualization     | matplotlib, seaborn                 |
| 14    | Next Steps        | CLI apps, packaging                 |

## Notebook Format Standard

Each notebook begins with:

- Title
- Learning Objectives (3–5)
- Prerequisites (links)
- Estimated Time
- Key Terms

Ends with:

- Summary
- Exercises (difficulty ★ to ★★★)
- Further Reading

## Contributing

See `CONTRIBUTING.md` for full guidelines. PRs welcome—especially improvements to clarity, exercises, and tests.

## Roadmap (Short-Term)

- [ ] Populate initial 10 notebooks (basics & control flow)
- [ ] Add notebook execution tests
- [ ] Publish docs site (MkDocs)
- [ ] Add exercises + solution reveal pattern

## License

GPL-3.0-only (see `LICENSE`). If you prefer a more permissive license (MIT/Apache) for broader reuse, open a discussion.

## Acknowledgments

Inspired by countless open educational resources. Contributions credited via Git history and CHANGELOG.

---

Happy learning! 🚀
