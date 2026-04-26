#!/usr/bin/env bash
set -euo pipefail

# Run focused PEP 8-style lint checks and print actionable output.
# Usage:
#   scripts/pep8_review.sh                # lint all Python files
#   scripts/pep8_review.sh app tests      # lint specific paths

if ! command -v ruff >/dev/null 2>&1; then
  echo "ruff is not installed. Install it with: pip install ruff"
  exit 1
fi

if [ "$#" -eq 0 ]; then
  echo "Running ruff on all tracked Python files..."
  ruff check .
else
  echo "Running ruff on: $*"
  ruff check "$@"
fi
