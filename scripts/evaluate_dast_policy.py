import json
import sys
import yaml

ZAP_REPORT = "zap-report.json"
POLICY_FILE = "policy/dast-gate.yml"

def load_policy():
    with open(POLICY_FILE, "r") as f:
        return yaml.safe_load(f)

def load_zap_report():
    with open(ZAP_REPORT, "r") as f:
        return json.load(f)

def main():
    policy = load_policy()
    report = load_zap_report()

    fail_levels = policy["enforcement"]["fail_on"]["risk_levels"]

    alerts = report.get("site", [{}])[0].get("alerts", [])
    violations = []

    for alert in alerts:
        if alert.get("risk") in fail_levels:
            violations.append(alert)

    if violations:
        print("Policy evaluation failed")
        for v in violations:
            print(f"- {v['alert']} (Risk: {v['risk']})")
        sys.exit(1)

    print("Policy evaluation passed")
    sys.exit(0)

if __name__ == "__main__":
    main()
