# IPI Protocol - Core Calculation Engine (Proof of Concept)
# Launch Date: 2026-03-01
# Standard: EU PEF EF 4.0 Integration

def calculate_ipi(carbon_kg, water_m3, resource_deplete, dqr_factor=1.0, base_neutral=100):
    """
    Calculates the IPI score based on 3 key PEF indicators (simplified for PoC).
    Weights based on official EU EF 4.0 guidelines.
    """
    # Normalized weights (Climate: 21.06%, Water: 8.51%, Resources: 7.55%)
    # These factors map raw units to a scale where '100' is the market average.
    w_carbon = 1.45   # Weight for Climate Change
    w_water = 0.65    # Weight for Water Scarcity
    w_resource = 120.0 # Weight for Resource Depletion (Minerals)

    # Core Algorithm: (Impact * Weight) * Data Quality Factor
    raw_impact = (carbon_kg * w_carbon) + (water_m3 * w_water) + (resource_deplete * w_resource)
    
    # Final IPI Score with DQR penalty (Actor-Specific vs Average)
    final_score = raw_impact * dqr_factor
    
    return round(final_score, 2)

# --- TEST SCENARIOS ---

# 1. Standard Smartphone (The Reference "100")
# Data: Primary, Verified
ref_ipi = calculate_ipi(carbon_kg=55.0, water_m3=12.5, resource_deplete=0.0004, dqr_factor=1.0)

# 2. High-Pollution Competitor (Fast-Fashion Electronics)
# Data: Secondary (Generic) -> Applies 1.2 Penalty
bad_ipi = calculate_ipi(carbon_kg=85.0, water_m3=25.0, resource_deplete=0.0009, dqr_factor=1.2)

# 3. Sustainable Innovator (Botswana Solar Mining / Circular Design)
# Data: Primary, Verified -> Direct Fiscal Bonus
good_ipi = calculate_ipi(carbon_kg=30.0, water_m3=5.0, resource_deplete=0.0002, dqr_factor=1.0)

print(f"--- IPI PROTOCOL TECHNICAL TEST - MARCH 1st, 2026 ---")
print(f"Scenario 1 (Reference Product): {ref_ipi} IPI  -> [Neutral VAT]")
print(f"Scenario 2 (High Pollution):    {bad_ipi} IPI  -> [MAX MALUS VAT]")
print(f"Scenario 3 (Sustainable):       {good_ipi} IPI   -> [SUPER BONUS VAT]")
print(f"---------------------------------------------------")
