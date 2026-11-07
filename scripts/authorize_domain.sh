#!/usr/bin/env bash
# Allow Google sign-in on the hosted site: add domains to Firebase Auth's authorized domains.
# Without this, sign-in on axomrank.pages.dev fails with auth/unauthorized-domain.
# Uses gcloud like deploy_rules.sh (no Firebase CLI needed). Safe to rerun: existing domains are kept.
# Usage: scripts/authorize_domain.sh [domain ...]     (defaults to axomrank.pages.dev)
set -euo pipefail
P="${AXOM_FIREBASE_PROJECT:-axomrank-ahom}"
DOMAINS=("${@:-axomrank.pages.dev}")
GCLOUD="$(command -v gcloud || echo "$HOME/google-cloud-sdk/bin/gcloud")"
TOKEN="$("$GCLOUD" auth print-access-token)"
H=(-H "Authorization: Bearer $TOKEN" -H "x-goog-user-project: $P" -H "Content-Type: application/json")
URL="https://identitytoolkit.googleapis.com/admin/v2/projects/$P/config"
CURRENT="$(curl -sf "${H[@]}" "$URL")"
BODY="$(python3 -c 'import json,sys; c=json.loads(sys.argv[1]); d=c.get("authorizedDomains",[]); d+= [x for x in sys.argv[2:] if x not in d]; print(json.dumps({"authorizedDomains": d}))' "$CURRENT" "${DOMAINS[@]}")"
curl -sf -X PATCH "${H[@]}" "$URL?updateMask=authorizedDomains" -d "$BODY" | python3 -c 'import json,sys; print("Authorized domains:", ", ".join(json.load(sys.stdin)["authorizedDomains"]))'
