import sys

exec(f"from .l{sys.argv[1]} import part{sys.argv[2]}")
