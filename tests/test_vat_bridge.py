import pytest
from src.vat_bridge import VATBridge

def test_vat_bin_assignment():
    """
    Ensure the IPI score correctly places a product into the 
    sovereign-defined tax bracket (Bin).
    """
    # Custom state configuration (e.g., EU Member State 2026)
    custom_bins = [
        {"threshold": 80.0, "rate": 0.055},  # Sustainable (Reduced)
        {"threshold": 120.0, "rate": 0.20},  # Standard
        {"threshold": 1000.0, "rate": 0.25} # High-Pollution (Surcharge)
    ]
    bridge = VATBridge(bins=custom_bins)
    
    # Test Tier A (Green Innovation)
    assert bridge.get_vat_by_bin(75) == 0.055
    # Test Tier B (Market Average)
    assert bridge.get_vat_by_bin(100) == 0.20
    # Test Tier C (Polluting Actor)
    assert bridge.get_vat_by_bin(130) == 0.25

def test_default_bins_if_none_provided():
    """
    The bridge should provide a robust default fiscal model 
    if no specific bins are defined by the user.
    """
    bridge = VATBridge()
    # Default Sustainable bin is < 80 at 5%
    assert bridge.get_vat_by_bin(50) == 0.05

def test_final_price_calculation_with_bins():
    """
    Verify the final consumer price (TTC) based on the assigned 
    VAT bin for a high-performing product.
    """
    bridge = VATBridge()
    # Price 100, IPI 70 -> Falls in < 80 bin (5% VAT)
    final_price = bridge.get_final_price(price_ht=100.0, ipi_score=70.0)
    assert final_price == 105.0