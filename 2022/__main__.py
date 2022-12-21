import sys
import os

if not 2 < len(sys.argv) < 5:
    print("Usage: python -m 2022 <day> <part>")
    sys.exit(1)

if len(sys.argv) == 4 and sys.argv[3].lower() in ("t", "test"):
    os.environ["AOC_TEST_INPUT"] = "true"
else:
    os.environ["AOC_TEST_INPUT"] = "false"

exec(f"from .l{sys.argv[1]} import part{sys.argv[2]}")
