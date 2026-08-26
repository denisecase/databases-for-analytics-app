# databases-for-analytics-app

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Databases for Analytics Project.

## Project Planning

When tables are structured and related, SQL is the recommended language.
SQL requires a database, but we can still enjoy the advantages of Python
for further analysis and visualization.

Use this repository to explore a database analytics workflow
using SQLite, SQL, pandas, and Python visualization.

See [exercises/](./exercises/).

## First, Make Sure Your Machine is Set Up

Complete
[**Workflow A: Set Up Your Machine**](https://denisecase.github.io/pro-analytics-02/)
and verify all steps.
A good foundation is critical and will have time later.
Things change, so be sure to follow the new process

## Get this Example Project

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
carefully.

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages,
and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have this example project
running on your machine.
A new file `project.log` will appear in the root project folder
and running the example script will print out:

```shell
===================================
END main() - Executed successfully!
===================================
```

## Initial Results

![First Chart](./docs/images/first-chart.png)

When you change the SQL query in the Python app, the resulting chart will change.

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details markdown>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

Open a machine terminal in your `Repos` folder,
change directory (cd) into the new folder,
and run `code .` to open only this project in VS Code:

```shell
git clone https://github.com/denisecase/databases-for-analytics-app

cd databases-for-analytics-app
code .
```

When VS Code opens, accept the Extension Recommendations
(click **`Install All`** or similar when asked).

### In a VS Code terminal

To set up a local project Python environment (managed by `uv`)
and align VS Code with it, run the following commands.

These are listed for convenience.
For best results, follow the detailed instructions in
[pro-analytics-02 guide](https://denisecase.github.io/pro-analytics-02/).

Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal**
in the root project folder.
Copy each command, paste into your terminal, and hit ENTER,
to run each command one at a time.

```shell
uv self update
uv python pin 3.14

uv python install
uv lock --upgrade
uv sync
```

If asked: "We noticed a new environment has been created.
Do you want to select it for the workspace folder?" Click **"Yes"**.
If successful, you'll see a new `.venv` folder appear in the root project folder.

Install and run pre-commit checks (twice if necessary as shown below):

```shell
uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made by pre-commit tasks
uv run pre-commit run --all-files
```

### Daily Workflow (Working With Python Project Code)

VS Code should have only this project open.
Open a VS Code terminal (menu: `Terminal` / `New Terminal`) and run:

```shell
git pull

# run the module
uv run python -m databases_for_analytics.app

# do chores
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

While editing project code and docs, repeat the commands above to
run files, check them, and rebuild docs as needed.

Save progress frequently.
Some tools may make changes;
you may need to **re-run git `add` and `commit`**
to ensure everything gets committed before pushing.

```shell
git add -A
git commit -m "your message here"
# repeat if changes were made (try the UP ARROW)
git add -A
git commit -m "your message here"

git push -u origin main
```

</details>

## Helpful Tips

- Use the **UP ARROW** and **DOWN ARROW** in the terminal
  to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Much Can Be Ignored

- You do not need to add to or modify `tests/`.
  Tests are recommended and provided for example only.
- Many files are silent helpers.
  [Explore](https://denisecase.github.io/professional-python-project-explainer/)
  as you like, but most files are never touched.
- You do NOT need to understand everything;
  let understanding build over time.

## As Needed

If VS Code does not automatically use the new `.venv` environment:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Python: Select Interpreter**.
3. Select the interpreter from this project's `.venv` folder.

If VS Code still does not recognize the environment or newly installed tools:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Developer: Reload Window**.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Documentation

- [Documentation](https://denisecase.github.io/databases-for-analytics-app/)

## Data Card

- [World Data Card](./docs/data-card.md)

## Annotations

- [.annotations/annotations.md](./.annotations/annotations.md)

## Citation

- [CITATION.cff](./CITATION.cff)

## License

This project is licensed under the [MIT License](./LICENSE).
