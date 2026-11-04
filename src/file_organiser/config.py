from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Settings:
    # the folder to organise
    source_dir: Path

    #folder to organise the files into
    dest_dir: Path

    # minimum number of characters to trust a classification
    min_text_char: int = 150

    # below this level the file is left in place as low confidence
    min_confidence: float = 0.35

    # most text that will be read from a file
    max_chars: int = 20_000

    # keep a copy of the file to prevent file loss during organising
    copy_instead_of_move: bool = True

    # shows what would happe, change nothing
    dry_run: bool = False

