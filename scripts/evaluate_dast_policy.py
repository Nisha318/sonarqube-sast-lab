#!/usr/bin/env python3
import json
import os
import sys

try:
    import yaml  # pyyaml
except ImportError:
    yaml = None


RISK_NORMALIZATION = {
    "0": "Informational",
    "1": "Low",
    "2": "Medium",
    "3": "High",
    "informational": "Informational",
    "info": "Informational",
    "low": "Low",
    "medium": "Medium",
    "med": "Medium",
    "high": "High",
}


def normalize_risk(value: str) -> str:
    if value is None:
        return "Informational"
    v = str(value).strip()
    if not v:
        return "Informational"

    # Common formats: "High (3)", "Medium (2)", "Low (1)", "Informational (0)"
    token = v.split()[0].lower()
    if token in RISK_NORMALIZATION:
        return RISK_NORMALIZATION[token]

    # Sometimes riskcode is numeric 0-3
    if v in RISK_NORMALIZATION:
        return RISK_NORMALIZATION[v]

    return "Informational"


def extract_alerts(zap_json: dict) -> list[dict]:
    """
    Supports common ZAP JSON structures produced by zap-baseline.py.
    We try a few shapes defensively.
    """
    alerts = []

    # Shape A: {"site":[{"alerts":[...]}]}
    if isinstance(zap_json.get("site"), list):
        for site in zap_json["site"]:
            site_alerts = site.get("alerts", [])
            if isinstance(site_alerts, list):
                alerts.extend(site_alerts)

    # Shape B: {"alerts":[...]}
    if not alerts and isinstance(zap_json.get("alerts"), list):
        alerts = zap_json["alerts"]

    return alerts


def count_by_risk(alerts: list[dict]) -> dict:
    counts = {"High": 0, "Medium": 0, "Low": 0, "Informational": 0}

    for a in alerts:
        # ZAP often has riskdesc like "Medium (2)" and/or riskcode like "2"
        risk = normalize_risk(a.get("riskdesc") or a.get("riskcode"))
        if risk not in counts:
            risk = "Informational"
        counts[risk] += 1

    return counts


def decide(counts: dict, policy: dict) -> tuple[str, list[str]]:
    fail_on = set(policy.get("rules", {}).get("fail_on", []))
    warn_on = set(policy.get("rules", {}).get("warn_on", []))

    reasons = []
    for r in ["High", "Medium", "Low", "Informational"]:
        if counts.get(r, 0) > 0:
            reasons.append(f"{r}: {counts[r]}")

    if any(counts.get(r, 0) > 0 for r in fail_on):
        return "FAIL", reasons
    if any(counts.get(r, 0) > 0 for r in warn_on):
        return "WARN", reasons
    return "PASS", reasons


def load_policy(path: str) -> dict:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Policy file not found: {path}")

    if yaml is None:
        raise RuntimeError(
            "PyYAML is not installed. Install it or update the workflow to pip install pyyaml."
        )

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: evaluate_dast_policy.py <policy_yaml> [zap_json_path] [output_json_path]")
        return 2

    policy_path = sys.argv[1]
    policy = load_policy(policy_path)

    zap_path = sys.argv[2] if len(sys.argv) >= 3 else policy.get("inputs", {}).get("zap_json")
    if not zap_path:
        print("ZAP JSON path not provided and not found in policy inputs.")
        return 2

    output_path = sys.argv[3] if len(sys.argv) >= 4 else "policy/dast-policy-result.json"

    if not os.path.exists(zap_path):
        print(f"ZAP JSON not found: {zap_path}")
        return 2

    with open(zap_path, "r", encoding="utf-8") as f:
        zap_json = json.load(f)

    alerts = extract_alerts(zap_json)
    counts = count_by_risk(alerts)
    decision, reasons = decide(counts, policy)

    result = {
        "policy": policy.get("policy", {}),
        "input": {"zap_json": zap_path},
        "counts": counts,
        "decision": decision,
        "reasons": reasons,
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))

    # Return codes: PASS=0, WARN=0 (non-blocking), FAIL=1
    if decision == "FAIL":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
