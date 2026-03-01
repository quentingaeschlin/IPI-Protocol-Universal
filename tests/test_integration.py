import pytest
from src.ipi_calculator import IPICalculator
from src.vat_bridge import VATBridge

def test_full_protocol_chain():
    """
    Test the full chain: Environmental Impact -> IPI Score -> VAT Bin -> Final Price.
    Scenario: A high-efficiency textile product.
    """
    calc = IPICalculator()
    # Define primary impacts (Low impact product)
    impacts = {
        "climate_change": 0.4, 
        "water_use": 0.2,
        "resource_use_minerals_metals": 0.0001
    }
    
    # 1. Calculate IPI (Should be < 80)
    ipi_score = calc.calculate(impacts, dqr="primary")
    assert ipi_score < 80.0
    
    # 2. Bridge to Fiscality (Should fall in the 5% VAT bin)
    bridge = VATBridge() # Using default bins (< 80 = 5%)
    vat_rate = bridge.get_vat_by_bin(ipi_score)
    assert vat_rate == 0.05
    
    # 3. Final Retail Price Check
    final_price = bridge.get_final_price(price_ht=100.0, ipi_score=ipi_score)
    assert final_price == 105.0
