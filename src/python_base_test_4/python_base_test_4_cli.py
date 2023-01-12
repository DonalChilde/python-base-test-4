"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Python Base Test 4."""


if __name__ == "__main__":
    main(prog_name="python-base-test-4")  # pragma: no cover