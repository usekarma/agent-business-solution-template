"""Example domain model. Replace this with your actual business concepts."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WorkRequest:
    """A small example of validated business input."""

    request_id: str
    value: int

    def __post_init__(self) -> None:
        if not self.request_id.strip():
            raise ValueError("request_id must not be blank")
        if self.value < 0:
            raise ValueError("value must be non-negative")
