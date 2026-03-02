from typing import Dict
from pydantic import BaseModel, field_validator

class IPIImpactData(BaseModel):
    """
    Data structure for IPI input validation.
    Ensures that only valid DQR types are processed.
    """
    impacts: Dict[str, float]
    dqr_type: str = "primary"

    @field_validator('dqr_type')
    @classmethod
    def validate_dqr(cls, v: str):
        allowed_types = ["primary", "secondary", "default"]
        if v not in allowed_types:
            raise ValueError(f"DQR must be one of {allowed_types}")
        return v

class IPICalculator:
    """
    Core IPI Scoring Engine.
    Implements the 16 Environmental Footprint (EF 4.0) impact categories 
    and applies official JRC weighting factors.
    """

    # Official EU EF 4.0 Weighting Factors (%)
    # Source: European Commission Joint Research Centre (JRC)
    WEIGHTING_FACTORS = {
        "climate_change": 21.06,
        "ozone_depletion": 6.31,
        "ionising_radiation": 5.01,
        "photochemical_ozone_formation": 4.78,
        "particulate_matter": 8.96,
        "human_toxicity_cancer": 2.13,
        "human_toxicity_non_cancer": 1.84,
        "acidification": 6.05,
        "eutrophication_freshwater": 2.80,
        "eutrophication_marine": 2.96,
        "eutrophication_terrestrial": 3.71,
        "ecotoxicity_freshwater": 1.92,
        "land_use": 7.94,
        "water_use": 8.51,
        "resource_use_minerals_metals": 7.55,
        "resource_use_fossils": 8.32
    }

    # Coefficients for Data Quality Rating (DQR) penalties
    DQR_COEFFICIENTS = {
        "primary": 1.0,      # Verified primary data (No penalty)
        "secondary": 1.2,    # Industry average data (+20% penalty)
        "default": 1.5       # Missing/Expired data (+50% penalty)
    }

    def calculate(self, input_impacts: Dict[str, float], functional_unit: float, dqr: str = "primary") -> float:
        """
        Calculates IPI per Service Unit (e.g., per wear, per carat, per kWh).
        This aligns the protocol with official EU PEFCR 'Functional Units'.
        """
        if functional_unit <= 0:
            raise ValueError("Functional units (durability/quantity) must be greater than zero.")

        weighted_sum = 0.0
        for cat, value in input_impacts.items():
            weight = self.WEIGHTING_FACTORS[cat]
            weighted_sum += value * (weight / 100)

        # IPI = Impact per Service Rendered
        # We normalize to 100 based on a reference service level
        ipi_score = (weighted_sum / functional_unit) * 100 
        
        penalty = self.DQR_COEFFICIENTS.get(dqr, 1.5)
        return round(ipi_score * penalty, 2)
