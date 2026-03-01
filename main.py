from src.ipi_calculator import IPICalculator
from src.vat_bridge import VATBridge

def run_market_simulation():
    print("--- PROJECT IPI: MARKET SIMULATION (March 1st, 2026) ---")
    print("Scenario: Smartphone Competition (Standard Price: €500.00 HT)")
    
    calc = IPICalculator()
    # Standard EU VAT Bins
    eu_bins = [
        {"threshold": 85.0, "rate": 0.055},  # Sustainable Bonus
        {"threshold": 115.0, "rate": 0.20},  # Standard Neutral
        {"threshold": float('inf'), "rate": 0.25} # Pollution Malus
    ]
    bridge = VATBridge(bins=eu_bins)
    
    # 1. THE GREEN INNOVATOR (Primary Data, High Efficiency)
    impacts_a = {"climate_change": 0.5, "water_use": 0.5, "resource_use_minerals_metals": 0.0002}
    ipi_a = calc.calculate(impacts_a, dqr="primary")
    price_a = bridge.get_final_price(500.0, ipi_a)

    # 2. THE MID RANGE PRODUCER (Primary Data, Average Efficiency)
    impacts_b = {"climate_change": 1.7, "water_use": 0.5, "resource_use_minerals_metals": 0.0002}
    ipi_b = calc.calculate(impacts_b, dqr="primary")
    price_b = bridge.get_final_price(500.0, ipi_b)
    
    # 3. THE LINEAR POLLUTER (Secondary Data, Average Efficiency)
    impacts_c = {"climate_change": 65.0, "water_use": 18.0, "resource_use_minerals_metals": 0.0006}
    ipi_c = calc.calculate(impacts_c, dqr="secondary")
    price_c = bridge.get_final_price(500.0, ipi_c)

    # DISPLAY RESULTS
    print(f"\nPRODUCT A (Sustainable):")
    print(f" > IPI Score: {ipi_a} | VAT Rate: {bridge.get_vat_by_bin(ipi_a)*100}%")
    print(f" > FINAL RETAIL PRICE: €{price_a}")

    print(f"\nPRODUCT B (Average):")
    print(f" > IPI Score: {ipi_b} | VAT Rate: {bridge.get_vat_by_bin(ipi_b)*100}%")
    print(f" > FINAL RETAIL PRICE: €{price_b}")

    print(f"\nPRODUCT C (Polluting):")
    print(f" > IPI Score: {ipi_c} | VAT Rate: {bridge.get_vat_by_bin(ipi_c)*100}%")
    print(f" > FINAL RETAIL PRICE: €{price_c}")
    
    price_diff = round(price_b - price_a, 2)
    print(f"\nRESULT: The sustainable choice is €{price_diff} cheaper for the consumer.")
    print("---------------------------------------------------------")

if __name__ == "__main__":
    run_market_simulation()
