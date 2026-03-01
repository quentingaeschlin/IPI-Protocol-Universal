import pytest
from src.ipi_calculator import IPICalculator

def test_neutral_product_returns_100():
    """
    A product whose impacts exactly match the Representative Product (RP) 
    benchmarks must return an IPI score of 100.0.
    """
    calc = IPICalculator()
    # Mocking impacts where each category equals 1.0 (the baseline)
    # Based on EU EF 4.0 weighting factors.
    impacts = {cat: 1.0 for cat in calc.WEIGHTING_FACTORS.keys()}
    
    # In a real scenario, the normalization would be more complex, 
    # but for this TDD stage, we expect the base reference to hit 100.
    assert calc.calculate(impacts) == 100.0

def test_dqr_penalty_application():
    """
    Using secondary data must apply a 20% pollution penalty (1.2 coefficient) 
    compared to verified primary data.
    """
    calc = IPICalculator()
    impacts = {cat: 1.0 for cat in calc.WEIGHTING_FACTORS.keys()}
    
    score_primary = calc.calculate(impacts, dqr="primary")
    score_secondary = calc.calculate(impacts, dqr="secondary")
    
    # We use pytest.approx to handle floating point precision
    assert score_secondary == pytest.approx(score_primary * 1.2)

def test_default_penalty_for_missing_data():
    """
    Failing to provide data or using expired certificates must trigger 
     the +50% Default Penalty (1.5 coefficient).
    """
    calc = IPICalculator()
    impacts = {cat: 1.0 for cat in calc.WEIGHTING_FACTORS.keys()}
    
    score_primary = calc.calculate(impacts, dqr="primary")
    score_default = calc.calculate(impacts, dqr="default")
    
    assert score_default == pytest.approx(score_primary * 1.5)

def test_invalid_category_raises_error():
    """
    The engine must reject any impact category that is not part of the 
    official 16 PEF categories defined by the JRC.
    """
    calc = IPICalculator()
    with pytest.raises(ValueError, match="Invalid PEF category"):
        calc.calculate({"non_existent_pollutant": 10.0})

def test_empty_impacts_raises_error():
    """
    The calculator should not process empty data sets.
    """
    calc = IPICalculator()
    with pytest.raises(ValueError):
        calc.calculate({})
