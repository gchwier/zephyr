# Copyright (c) 2026 Nordic Semiconductor ASA
#
# SPDX-License-Identifier: Apache-2.0
import logging
import time

import pytest
from twister_harness import DeviceAdapter

logger = logging.getLogger(__name__)


def test_basic(dut: DeviceAdapter) -> None:

    time.sleep(3)
    lines = dut.readlines()
    pytest.LineMatcher(lines).fnmatch_lines([
        "*thread_a: Hello World from*",
        "*thread_b: Hello World from*"
    ])
