import json
import sys
from src import IPICalculator, VATBridge

def compare_geopolitics(case_study_path: str, state_a_path: str, state_b_path: str):
    """
    Geopolitical Comparison Engine.
    Loads a case study and compares two different national tax policies.
    """
    try:
        with open(case_study_path) as f: case_data = json.load(f)
        with open(state_a_path) as f: state_a = json.load(f)
        with open(state_b_path) as f: state_b = json.load(f)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    calc = IPICalculator()
    bridge_a = VATBridge(bins=state_a["tax_bins"])
    bridge_b = VATBridge(bins=state_b["tax_bins"])

    print(f"\n🌍 IPI GEOPOLITICAL COMPARISON: {case_data['metadata']['scenario_name']}")
    print(f"Policy: {state_a['state_name']} vs {state_b['state_name']}")
    print("=" * 95)
    
    header = f"{'Product Name':<25} | {'IPI':<7} | {'Net (HT)':<10} | {state_a['state_name']:<20} | {state_b['state_name']:<20}"
    print(header)
    print("-" * 95)

    for prod in case_data["products"]:
        # IPI Calculation (Normalized by Functional Unit)
        rp_benchmark = case_data["metadata"]["rp_benchmark"]

        ipi = calc.calculate(
            prod["impacts"], 
            functional_unit=prod["functional_unit"], 
            rp_benchmark=rp_benchmark,
            dqr=prod["dqr_type"]
        )
        
        price_ht = prod["base_price_ht"]
        price_a = bridge_a.get_final_price(price_ht, ipi)
        price_b = bridge_b.get_final_price(price_ht, ipi)

        print(f"{prod['name']:<25} | {ipi:<7.2f} | €{price_ht:<9} | €{price_a:<19} | €{price_b:<19}")

    print("=" * 95)
    print("Strategic Note: State B effectively neutralizes the price gap for sustainable goods.")

if __name__ == "__main__":
    # --- CLI ARGUMENT LOGIC ---
    # Default paths
    default_case = "data/case_study_textile.json"
    default_state_a = "data/state_a_pragmatic.json"
    default_state_b = "data/state_b_radical.json"

    # Override defaults if arguments are provided via terminal
    case_arg = sys.argv[1] if len(sys.argv) > 1 else default_case
    state_a_arg = sys.argv[2] if len(sys.argv) > 2 else default_state_a
    state_b_arg = sys.argv[3] if len(sys.argv) > 3 else default_state_b

    compare_geopolitics(case_arg, state_a_arg, state_b_arg)
