#!/bin/bash

set -e

${BLACK:-black} bin/ breakoutgardenexporter/ tests/

MYPYPATH=./stubs:$MYPYPATH mypy -m breakoutgardenexporter

MYPYPATH=./stubs:$MYPYPATH mypy -m tests

MYPYPATH=./stubs:$MYPYPATH mypy bin/*
