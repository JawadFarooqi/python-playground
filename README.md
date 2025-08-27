<div align="center">
	<h1>Python Playground</h1>
	<p><strong>A structured learning journey through Python fundamentals to AI/ML concepts with 30 interactive Jupyter notebooks.</strong></p>
	<p>
		<a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-GPLv3-blue.svg"></a>
		<a href=".github/workflows/ci.yml"><img alt="CI" src="https://github.com/JawadFarooqi/python-playground/actions/workflows/ci.yml/badge.svg"></a>
	</p>
</div>

## About This Project

This repository provides a structured path for learning Python through 30 carefully organized Jupyter notebooks, progressing from basic syntax to advanced topics including data science and AI/ML fundamentals.

**What You'll Find:**

- **Clear Learning Path:** 30 notebooks organized across 6 progressive sections
- **Hands-On Learning:** Interactive code examples and practice exercises
- **Modern Python:** Current best practices and real-world applications
- **Comprehensive Scope:** From Python basics through AI/ML introductions

## Quick Start (Pick ONE path)

### 1. Fastest (just look & run a first notebook)

You only need Python 3.11+ installed.

```bash
git clone https://github.com/JawadFarooqi/python-playground.git
cd python-playground
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install --upgrade pip
pip install notebook
jupyter notebook
```

Then open `notebooks/` and start with `01_getting_started.ipynb`.

### 2. Recommended (with helper tools & tests)

```bash
git clone https://github.com/JawadFarooqi/python-playground.git
cd python-playground
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]  # install package + dev tools
pre-commit install      # optional: auto-fix style on commit
jupyter notebook
```

### 3. One-liner (using uv — optional fast resolver)

If you have `uv` installed:

```bash
uv sync --all-extras
uv run jupyter notebook
```

If you only want to browse notebooks online (no install), you will later be able to use an nbviewer or Binder badge (coming soon).

> New to virtual environments? Think of `.venv` as a private folder where this project keeps its own tools so they don't clash with other projects.

## Repository Layout

```
src/playground/    # Reusable helper utilities imported by notebooks
notebooks/         # 30 progressive learning notebooks organized in 6 tracks
  01_foundation/     # Notebooks 1-5: Python basics
  02_core_skills/    # Notebooks 6-10: Functions, data structures
  03_intermediate/   # Notebooks 11-15: OOP, file handling, error handling
  04_advanced/       # Notebooks 16-20: Advanced Python, project development
  05_data_science/   # Notebooks 21-25: NumPy, pandas, visualization
  06_ai_machine_learning/  # Notebooks 26-30: ML, deep learning, AI applications
tests/             # Pytest-based tests (unit + notebook smoke tests)
docs/              # Documentation site sources
.github/           # CI workflows, issue templates, PR template
```

## Learning Path Structure

**🎯 Learning Journey:** Master Python fundamentals → Explore data science → Discover AI/ML concepts

| Section          | Notebooks | Focus Area               | What You'll Learn                                    |
| ---------------- | --------- | ------------------------ | ---------------------------------------------------- |
| **Foundation**   | 1-5       | Python Essentials        | Syntax, variables, operations, basic programming     |
| **Core Skills**  | 6-10      | Programming Fundamentals | Loops, functions, data structures, control flow      |
| **Intermediate** | 11-15     | Structured Programming   | OOP, file handling, error management, debugging      |
| **Advanced**     | 16-20     | Professional Development | Modules, packages, testing, best practices           |
| **Data Science** | 21-25     | Data Analysis            | NumPy, pandas, visualization, data workflows         |
| **AI & ML**      | 26-30     | Machine Learning         | ML fundamentals, neural networks, modern AI concepts |

**📈 Track Your Progress:** Use `learning_plan.md` for detailed learning objectives and completion tracking.

## Notebook Design

Each notebook follows a consistent learning-focused structure:

- **Clear Objectives:** Know exactly what you'll learn and achieve
- **Step-by-Step Examples:** Code demonstrations with detailed explanations
- **Practice Exercises:** Reinforce concepts through hands-on coding
- **Real-World Applications:** See how concepts apply to actual problems
- **Progress Summaries:** Review and solidify your understanding

Perfect for self-paced learning with measurable progress at each step.

## How to Use This Repository

1. **Start Fresh:** Follow the setup instructions to get your environment ready
2. **Begin with Foundations:** Start with notebook 1 and work sequentially
3. **Practice Actively:** Run all code examples and complete the exercises
4. **Build Understanding:** Each notebook builds on concepts from previous ones
5. **Track Your Journey:** Use `learning_plan.md` to mark your progress

**Recommended Approach:** Dedicate focused time to each notebook, ensuring you understand concepts before moving forward.

## Contributing

We welcome contributions that help improve the learning experience! Areas where you can make an impact:

- **Content Enhancement:** Improve explanations, add examples, create exercises
- **Code Quality:** Fix bugs, optimize examples, ensure best practices
- **Learning Experience:** Suggest improvements to notebook flow and structure
- **Documentation:** Help make instructions clearer and more comprehensive

See `CONTRIBUTING.md` for detailed guidelines on how to get involved.

## Learning Outcomes

Successfully working through this repository will give you:

- **Strong Python Foundation:** Solid understanding of Python syntax, concepts, and best practices
- **Problem-Solving Skills:** Ability to break down problems and implement solutions
- **Data Science Readiness:** Preparation for data analysis and visualization work
- **AI/ML Awareness:** Understanding of machine learning concepts and modern AI applications
- **Professional Development:** Knowledge of tools and practices used in real-world Python development

This foundation prepares you for advanced studies, professional development, or specialized training in areas like data science, machine learning, or software engineering.

## Project Status & Roadmap

**Foundation Established:**

- ✅ Complete repository structure with organized 30-notebook framework
- ✅ Comprehensive learning plan with clear progression and completion criteria
- ✅ Foundation notebooks ready for learning Python basics

**Active Development:**

- 🔄 Expanding content across all notebook sections
- 🔄 Adding interactive exercises and practical projects
- 🔄 Implementing testing and validation for all examples

**Future Enhancements:**

- 📋 Advanced project-based learning modules
- 📋 Interactive assessments and progress tracking
- 📋 Community features and collaborative learning tools
- 📋 Integration with online learning platforms

## License

GPL-3.0-only (see `LICENSE`). If you prefer a more permissive license (MIT/Apache) for broader reuse, open a discussion.

## Acknowledgments

Inspired by countless open educational resources. Contributions credited via Git history and CHANGELOG.

---

Happy learning! 🚀
