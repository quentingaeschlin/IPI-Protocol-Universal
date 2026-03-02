import pytest
import json
from src.ipi_calculator import IPICalculator
from src.vat_bridge import VATBridge

def test_full_protocol_integration_from_json():
    """
    Test the full chain using the standardized JSON format and functional Unit.
    Scenario: Circular-Local T-Shirt (High durability/functional unit).
    """
    # 1. Load the unified JSON data
    json_path = "data/case_study_textile.json"
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # 2. Extract the high-performance product
    product = data["products"][0] 
    assert product["name"] == "Circular-Local T-Shirt"
    assert "functional_unit" in product
    
    # 3. Initialize Engines
    calc = IPICalculator()
    bridge = VATBridge(bins=data["fiscal_config"]["tax_bins"])
    
    # 4. Verification of the "functional-Unit logic
    # The IPI must be calculated PER functional UNIT(e.g., per wear)
    ipi_score = calc.calculate(
        product["impacts"], 
        functional_unit=product["functional_unit"], 
        dqr=product["dqr_type"]
    )
    
    # 5. Fiscal result
    vat_rate = bridge.get_vat_by_bin(ipi_score)
    final_price = bridge.get_final_price(product["base_price_ht"], ipi_score)
    
    # Assertions: 
    # High durability (80 wears) should result in a very low IPI
    assert ipi_score < 50.0 
    assert vat_rate == 0.055  # Should fall into the sustainable bin
    assert final_price == pytest.approx(25.0 * 1.055, abs=0.01)
