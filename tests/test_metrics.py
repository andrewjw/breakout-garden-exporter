#!/usr/bin/env python3
# breakout-garden-exporter
# Copyright (C) 2023 Andrew Wilkinson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from breakoutgardenexporter import Metrics, COUNTER


class TestMetrics(unittest.TestCase):
    def test_create_and_set_metric(self):
        metrics = Metrics()
        metrics.add_metric("test_metric", COUNTER, "Test Metric")
        metrics.set("test_metric", "tag=1", 1.0)

        self.assertIn("test_metric{tag=1} 1.0", str(metrics))

    def test_clear_metric(self):
        metrics = Metrics()
        metrics.add_metric("test_metric", COUNTER, "Test Metric")
        metrics.set("test_metric", "tag=1", 1.0)
        metrics.clear("test_metric", "tag=1")

        self.assertNotIn("test_metric{tag=1} 1.0", str(metrics))

        # Check double clears don't fail.
        metrics.clear("test_metric", "tag=1")
