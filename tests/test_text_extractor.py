from pathlib import Path
from file_organiser.extractors.text import PlainTextExtractor

FIXTURE = Path(__file__).parent / "fixtures"
def test_reads_text_from_finance_fixture():
    extractor = PlainTextExtractor()
    text = extractor.extract(FIXTURE / "finance_clear.txt", max_chars=5000)
    assert "payment" in text.lower()

# check that extractor respects the max_chars limit
def test_follows_max_chars_limit(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("a" * 100, encoding="utf-8")
    extractor = PlainTextExtractor()
    text = extractor.extract(f, max_chars=50)
    assert len(text) == 50