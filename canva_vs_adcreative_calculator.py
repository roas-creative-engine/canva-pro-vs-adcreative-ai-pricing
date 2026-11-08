#!/usr/bin/env python3
"""
Canva Pro + Designer vs AdCreative.ai Production Cost Calculator 2026.
Models graphic design labor plus software overhead against automated AI generation.
"""
import argparse

def calculate_comparison(canva_sub, designer_retainer, adcreative_sub, review_overhead):
    manual_monthly = canva_sub + designer_retainer
    adcreative_monthly = adcreative_sub + review_overhead
    monthly_savings = manual_monthly - adcreative_monthly
    annual_savings = monthly_savings * 12.0
    return {
        "manual_monthly": manual_monthly,
        "adcreative_monthly": adcreative_monthly,
        "monthly_savings": monthly_savings,
        "annual_savings": annual_savings
    }

def main():
    parser = argparse.ArgumentParser(description="Canva Pro vs AdCreative.ai Production Comparison")
    parser.add_argument("--canva-sub", type=float, default=15.0, help="Canva Pro subscription in USD (default: $15.00)")
    parser.add_argument("--designer-retainer", type=float, default=500.0, help="Freelance designer monthly retainer in USD (default: $500.00)")
    parser.add_argument("--adcreative-sub", type=float, default=149.0, help="AdCreative.ai monthly fee in USD (default: $149.00)")
    parser.add_argument("--review-overhead", type=float, default=60.0, help="In-house QA review overhead in USD (default: $60.00)")
    args = parser.parse_args()

    res = calculate_comparison(args.canva_sub, args.designer_retainer, args.adcreative_sub, args.review_overhead)
    print(f"Manual Design Stack:     ${res['manual_monthly']:.2f}/mo")
    print(f"AdCreative.ai Pipeline:  ${res['adcreative_monthly']:.2f}/mo")
    print(f"Monthly Production Save: ${res['monthly_savings']:.2f}/mo")
    print(f"Annual Projected Savings:${res['annual_savings']:.2f}/year")

if __name__ == "__main__":
    main()
