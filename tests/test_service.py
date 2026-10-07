from __future__ import annotations

import pytest

from business_app.domain import WorkRequest
from business_app.service import calculate_result


def test_calculate_result() -> None:
    request = WorkRequest(request_id="req-1", value=21)

    assert calculate_result(request) == 42


def test_request_id_must_not_be_blank() -> None:
    with pytest.raises(ValueError, match="request_id"):
        WorkRequest(request_id=" ", value=1)


def test_value_must_not_be_negative() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        WorkRequest(request_id="req-1", value=-1)
