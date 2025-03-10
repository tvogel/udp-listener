#!/bin/bash
OLD_LOG="$2"

if [ -f "$OLD_LOG" ]; then
  zstd --rm "$OLD_LOG"
fi
