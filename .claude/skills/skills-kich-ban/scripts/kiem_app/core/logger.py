import sys

class Logger:
    def info(self, message: str):
        print(f"[INFO] {message}")

    def error(self, message: str):
        print(f"[ERROR] {message}", file=sys.stderr)

    def success(self, message: str):
        print(f"[PASS] {message}")

    def fail(self, message: str):
        print(f"[FAIL] {message}", file=sys.stderr)
