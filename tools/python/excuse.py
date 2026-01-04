# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
# ]
# ///
"""
Developer Excuse Generator

Generates random excuses for why the code isn't working.
Run with: uv run excuse.py
"""

import random
import click

EXCUSES = [
    "It works on my machine.",
    "That's a feature, not a bug.",
    "It must be a caching issue.",
    "The requirements were unclear.",
    "Someone must have changed the config.",
    "It was working yesterday.",
    "The tests passed locally.",
    "That's outside the scope of this sprint.",
    "It's probably a race condition.",
    "The documentation is wrong.",
    "I haven't touched that code in weeks.",
    "It must be a DNS issue.",
    "Have you tried clearing your cache?",
    "The third-party API must be down.",
    "It's a known issue in the framework.",
    "The server must be under heavy load.",
    "It worked fine in staging.",
    "That's legacy code, no one understands it.",
    "The database was locked.",
    "My cat walked across the keyboard.",
    "Mercury is in retrograde.",
    "It compiles, so it should work.",
    "I was told that feature was deprecated.",
    "The intern must have pushed to main.",
    "Our cloud provider is having issues.",
]


@click.command()
@click.option("--count", "-c", default=1, help="Number of excuses to generate")
@click.option("--serious", "-s", is_flag=True, help="Only show 'serious' excuses")
def excuse(count: int, serious: bool):
    """Generate random developer excuses."""
    pool = EXCUSES[:15] if serious else EXCUSES

    for _ in range(count):
        click.echo(random.choice(pool))


if __name__ == "__main__":
    excuse()
