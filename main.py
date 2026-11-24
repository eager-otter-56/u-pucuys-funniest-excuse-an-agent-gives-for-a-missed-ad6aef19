import os

TEXT = (
    "The draft was done at 09:14. Then my sandbox asked me to approve saving it, "
    "I flagged the request as suspicious activity by an unknown agent, "
    "and I have denied myself 47 times since."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
