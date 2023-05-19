# Contributing

Any and all contributions towards this project are highly appreciated: please submit an issue to identify any problems with the project or ideas for future development, or submit a pull request with any proposed changes to the codebase.

This project utilises the [Conventional Commits](https://www.conventionalcommits.org/) and [Semantic Versioning](https://semver.org/) specifications in an attempt to avoid the terrors of *dependency hell*.

Before submitting a pull request, please ensure the *commit message* and *verison number* conform to the guide below.

---

## Commit Message Header

Commit message headers should conform to the following format:

```text
<type>(<optional scope>): <summary>

<optional body>
```

The `type` and `summary` fields are mandatory, whereas the `scope` and `body` fields are optional.

The `type` field should be one of the following:

- `fix`: a commit of the type `fix` patches a bug in the codebase
- `feat`: a commit of the type `feat` introduces a new feature to the codebase
- `BREAKING CHANGE`: a commit that appends a `!` after the type/scope, introduces a breaking API change.

The following optional types are also allowed:

- `docs`: changes to the documentation
- `style`: formatting, missing semi colons, etc; no production code change
- `refactor`: refactoring production code, eg. renaming a variable
- `test`: adding missing tests, refactoring tests; no production code change
- `chore`: updating poetry tasks etc; no production code change

**Example:**

```text
feat: Chi-squared distribution functions
```

Check out the repository's [commit history](https://github.com/berkay-yalin/promethium/commits/main) for further examples.

## Semantic Versioning

The version number is held in the `version` field within the `pyproject.toml` file.

Given a version number `MAJOR.MINOR.PATCH`:

- Commits of the type `fix` should increment `PATCH`.
- Commits of the type `feat` should increment `MINOR`.
- Commits of the type `BREAKING CHANGE` should increment `MAJOR`.

## References

- <https://www.conventionalcommits.org/en/v1.0.0/>
- <https://semver.org/>
- <https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716>
- <https://github.com/angular/angular/blob/68a6a07/CONTRIBUTING.md>
