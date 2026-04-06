def load_text(path: str) -> str:
    file_path = Path(path)

    # if file doesn't exist OR invalid path → fallback to sample.txt
    if not file_path.exists():
        fallback = Path("data/sample.txt")
        if fallback.exists():
            return fallback.read_text(encoding="utf-8")
        return ""  # safe fallback if even sample missing

    return file_path.read_text(encoding="utf-8")