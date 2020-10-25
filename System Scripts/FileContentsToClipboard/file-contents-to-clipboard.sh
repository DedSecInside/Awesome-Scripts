#!/usr/bin/env bash

typeset -r arg="$1"

if [[ "$OSTYPE" == "darwin"*  ]]; then # For macos
  cat "$arg" | pbcopy;
else
  cat "$arg" | xsel --clipboard --input;
fi
