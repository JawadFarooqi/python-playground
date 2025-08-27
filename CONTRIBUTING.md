# Contributing

Thanks for your interest in improving this Python learning playground!

## Ways to contribute

- Improve existing notebooks (clarity, typos, examples)
- Add new beginner-friendly notebooks (follow naming & template)
- Add or refine utility helpers in `src/playground`
- Create or improve tests
- File issues: bugs, enhancement ideas, exercise suggestions

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install --upgrade pip
pip install .[dev]
pre-commit install
```

### Absolute beginner shortcut
If you only want to run notebooks (no tests/tooling yet):
```bash
python -m venv .venv
source .venv/bin/activate
pip install notebook
jupyter notebook
```
Or run: `bash scripts/bootstrap.sh`

## Notebook guidelines

Each notebook must include at the top:

1. Title
2. Learning objectives (3–5 bullet points)
3. Prerequisites (links to earlier notebooks)
4. Estimated time

And at the bottom:

- Summary
- 3–5 practice exercises
- Further reading links

Keep outputs minimal; prefer showing only what reinforces a concept. Avoid long-running cells.

## Naming

```
NN_topicGroup/NN_descriptive_title.ipynb
```

Example: `03_functions/02_args_kwargs.ipynb`

## Style

- Follow PEP 8 (enforced by Ruff/Black)
- Prefer type hints in shared utilities
- Small, focused examples; avoid “magic numbers” (use named vars)

## Tests

Run tests & lint before pushing:

```bash
pytest -q
ruff check .
black --check .
```

## Pull requests

PR template checklist will remind you to:

- Add notebook metadata sections
- Strip unnecessary outputs
- Link prerequisites
- Update README index if adding a new notebook

## License

By contributing, you agree your contributions are licensed under the repository license (GPL-3.0-only unless changed).
