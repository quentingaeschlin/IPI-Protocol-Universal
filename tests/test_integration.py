import pytest
import json
from src import IPICalculator, VATBridge

def test_geopolitical_integration_state_a_vs_b():
    """
    Test the full chain for both State A (Pragmatic) and State B (Radical).
    Scenario: Circular-Local T-Shirt.
    """
    # 1. Load Data
    with open("data/case_study_textile.json") as f: case_data = json.load(f)
    with open("data/state_a_pragmatic.json") as f: state_a = json.load(f)
    with open("data/state_b_radical.json") as f: state_b = json.load(f)
    
    # 2. Extract Product (Circular-Local)
    product = case_data["products"][0] 
    rp_ref = case_data["metadata"]["rp_benchmark"]
    assert product["name"] == "Circular-Local T-Shirt"
    
    # 3. Setup Engines
    calc = IPICalculator()
    bridge_a = VATBridge(bins=state_a["tax_bins"])
    bridge_b = VATBridge(bins=state_b["tax_bins"])
    
    # 4. Calculate IPI
    ipi_score = calc.calculate(
        product["impacts"], 
        functional_unit=product["functional_unit"], 
        rp_benchmark=rp_ref,
        dqr=product["dqr_type"]
    )
    
    # 5. Verify Price in State A (Pragmatic: 5.5% VAT)
    price_a = bridge_a.get_final_price(product["base_price_ht"], ipi_score)
    assert price_a == pytest.approx(26.38, abs=0.01)
    
    # 6. Verify Price in State B (Radical: 0% VAT / Price Parity)
    price_b = bridge_b.get_final_price(product["base_price_ht"], ipi_score)
    assert price_b == 25.0  # Perfect parity for sustainable goods
