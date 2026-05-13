def dupont_analysis(name, net_income, ebt, ebit, sales, assets, equity):
    # 5-Step Components
    tax_burden = net_income / ebt
    interest_burden = ebt / ebit
    operating_margin = ebit / sales
    asset_turnover = sales / assets
    leverage = assets / equity
    
    # Calculation
    roe = tax_burden * interest_burden * operating_margin * asset_turnover * leverage
    
    print(f"\n--- Analysis for {name} ---")
    print(f"{'Step':<20} | {'Value':<10} | {'Meaning'}")
    print("-" * 60)
    print(f"{'1. Tax Burden':<20} | {tax_burden:10.2f} | % of profit kept after taxes")
    print(f"{'2. Interest Burden':<20} | {interest_burden:10.2f} | % of EBIT kept after interest")
    print(f"{'3. Operating Margin':<20} | {operating_margin:10.2%} | Efficiency of core operations")
    print(f"{'4. Asset Turnover':<20} | {asset_turnover:10.2f} | Sales generated per Euro of Assets")
    print(f"{'5. Leverage':<20} | {leverage:10.2f} | Assets controlled per Euro of Equity")
    print("-" * 60)
    print(f"{'FINAL ROE':<20} | {roe:10.2%} | Return on Equity")

if __name__ == "__main__":
    print("="*60)
    print("           PRACTICAL DUPONT ANALYSIS EXAMPLE")
    print("="*60)
    
    # COMPANY A: "The Supermarket" (Lidl style)
    # Low margins (3%), but very high turnover (3.0x)
    dupont_analysis(
        name="Company A (High Volume)",
        net_income=2100, ebt=3000, ebit=3500, sales=100000, assets=33333, equity=10000
    )
    
    # COMPANY B: "The Luxury Brand" (Ferrari style)
    # High margins (25%), but slow turnover (0.4x)
    dupont_analysis(
        name="Company B (High Margin)",
        net_income=6300, ebt=9000, ebit=10000, sales=40000, assets=100000, equity=50000
    )
    
    print("\n" + "="*60)
    print("EXAM NOTE: Notice how Company A reaches a 21% ROE despite low margins")
    print("by moving inventory very fast. Company B reaches 12.6% ROE by focusing")
    print("on high-profit sales even if they move slowly.")
