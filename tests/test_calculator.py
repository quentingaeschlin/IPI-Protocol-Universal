import re
import pytest
from src.ipi_calculator import IPICalculator

def test_neutral_product_returns_100():
    """
    A product whose impacts match the reference benchmarks 
    per functional unitmust return an IPI of 100.
    """
    calc = IPICalculator()
    # Impacts scaled to 1.0 per unit
    impacts = {cat: 1.0 for cat in calc.WEIGHTING_FACTORS.keys()}
    
    # We define 1.0 functional unit(e.g., 1 wear or 1 carat)
    assert calc.calculate(impacts, functional_unit=1.0) == pytest.approx(100.0, rel=2e-3)

def test_durability_impact_on_score():
    """
    Increasing functional unit (durability) must mechanically 
    lower the IPI score for the same total impact.
    """
    calc = IPICalculator()
    impacts = {cat: 1.0 for cat in calc.WEIGHTING_FACTORS.keys()}
    
    # Product with 1 functional_unit vs Product with 2 functional_unit
    score_low_durability = calc.calculate(impacts, functional_unit=1.0)
    score_high_durability = calc.calculate(impacts, functional_unit=2.0)
    
    # The score should be exactly half (50 vs 100)
    assert score_high_durability == pytest.approx(score_low_durability / 2, abs = 0.01)

def test_dqr_penalty_application():
    """
    Using secondary data must apply the +20% penalty on the 
    functional-unitnormalized score.
    """
    calc = IPICalculator()
    impacts = {cat: 1.0 for cat in calc.WEIGHTING_FACTORS.keys()}
    
    score_primary = calc.calculate(impacts, functional_unit=1.0, dqr="primary")
    score_secondary = calc.calculate(impacts, functional_unit=1.0, dqr="secondary")
    
    assert score_secondary == pytest.approx(score_primary * 1.2)

def test_invalid_functional_unit_raises_error():
    """
    The engine must reject zero or negative functional unit.
    """
    calc = IPICalculator()
    impacts = {"climate_change": 10.0}
    with pytest.raises(ValueError, match=re.escape("Functional units (durability/quantity) must be greater than zero.")):
        calc.calculate(impacts, functional_unit=0)
