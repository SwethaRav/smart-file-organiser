# This file sets ups the data models for the file organiser - so that it's easier to use and reduce bugs later on
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

# Class for defining the outcomes after the organiser was run
class Outcome(str, Enum):
    ORGANISED = "organised"
    LEFT_IN_PLACE = "left_in_place"

# Class Reason for defining the reasons why a file was left in place, same outcome but different message to help with debugging later
class Reason(str, Enum):
    NO_USABLE_TEXT = "no_usable_text"
    LOW_CONFIDENCE = "low_confidence"
    UNSUPPORTED_TYPE = "unsupported_type"
    EXTRACTION_FAILED = "extraction_failed"

# Class for determining which folder it chooses and how sure it is (confidence)
# will add more fields to this class to help with debugging later
@dataclass(frozen=True)
class Classification:
    label: str
    confidence: float

# what the process () returns. The CLI decides how to display it
@dataclass(frozen=True)
class PipelineResult:
    path: Path
    outcome: Outcome
    label: str | None = None
    reason: Reason | None = None
    destination: Path | None = None
    detail: str = ""