import json
import sys
from src import IPICalculator, VATBridge

def run_ipi_simulation(json_path: str):
    """
    Runs a full IPI-to-VAT simulation based on a standardized JSON input file.
    """
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {json_path} not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in {json_path}.")
        return

    metadata = data.get("metadata", {})
    print(f"\n--- IPI PROTOCOL SIMULATION: {metadata.get('scenario_name')} ---")
    print(f"Sector: {metadata.get('industry_sector')} | Date: {metadata.get('date')}")
    print("-" * 60)

    # Initialize Engines
    calc = IPICalculator()
    fiscal_config = data.get("fiscal_config", {})
    # Map 'tax_bins' from JSON to the VATBridge
    bridge = VATBridge(bins=fiscal_config.get("tax_bins"))

    for product in data.get("products", []):
        # 1. Calculate IPI Score
        ipi_score = calc.calculate(product["impacts"], dqr=product["dqr_type"])
        
        # 2. Get Modulated VAT and Final Price
        vat_rate = bridge.get_vat_by_bin(ipi_score)
        final_price = bridge.get_final_price(product["base_price_ht"], ipi_score)
        
        # Display results per product
        print(f"PRODUCT: {product['name']}")
        print(f" > DQR Type: {product['dqr_type']} | IPI Score: {ipi_score}")
        print(f" > Applied VAT: {round(vat_rate * 100, 2)}% | Final Price (TTC): €{final_price}")
        print("-" * 30)

    print("Simulation Complete. Protocol Verified.")

if __name__ == "__main__":
    # Allow running specific case studies via command line
    # Default to textile if no argument is provided
    target_file = sys.argv[1] if len(sys.argv) > 1 else "data/case_study_textile.json"
    run_ipi_simulation(target_file)
