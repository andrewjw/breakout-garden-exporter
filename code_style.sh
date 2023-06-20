#!/bin/bash

set -e

${PYCODESTYLE:-pycodestyle} bin/ breakout-garden-exporter/ tests/
