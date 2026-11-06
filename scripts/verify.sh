#!/usr/bin/env bash
# Run the build and every automated check. Stops at the first failure.
# Usage: scripts/verify.sh
# This does not prove historical accuracy, fluent Assamese or browser behaviour:
# new units still need audit_lessons.py, and player changes need autoplay.js.
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONDONTWRITEBYTECODE=1

python3 scripts/build.py
python3 scripts/check_math.py
python3 scripts/check_reasoning.py
python3 scripts/check_constitution.py
python3 scripts/check_indian_history.py
python3 scripts/check_history_completion.py
python3 scripts/check_asof.py
node scripts/check_daily_review.cjs
node scripts/check_learning_gates.cjs
node scripts/check_skill_model.cjs
echo "verify: all checks passed"
