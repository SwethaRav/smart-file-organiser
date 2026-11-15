from pathlib import Path
class PlainTextExtractor:
    def extract(self, path: Path, max_chars: int) -> str:
        with path.open("r", encoding="utf-8") as file:
            text = file.read(max_chars)
        return text
