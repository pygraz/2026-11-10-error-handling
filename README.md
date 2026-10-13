# Error handling

Slides and code for the meetup session on error handling, organized as collaboration between [PyGraz](https://pygraz.org/) and [UX Graz](https://uxgraz.at/).

## Slides

The slides are located in:

- Error handling.pdf: The PDF version of the slides
- Error handling.key: The editable Keynote presentation

## Code examples

The easiest way to toy with the code example is to open the project in [PyCharm](https://www.jetbrains.com/pycharm/).

If you prefer to work in the terminal, proceed as follows:

Install [uv](https://docs.astral.sh/uv/).

Set up the Python project:

```bash
uv sync --all-groups
```

Install the pre-commit hooks for linting the source code:

```bash
uv run prek install
```

Run an example, for instance:

```bash
uv run sum_lines numbers.txt
```

## License

Error handling © 2026 by [Thomas Aglassinger](https://roskakori.at) and Jakob Schurrer is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
