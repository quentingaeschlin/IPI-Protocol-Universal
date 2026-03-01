# 🧮 Core Algorithm: The IPI Scoring Engine
**Protocol Version:** 1.0.0-beta  
**Standard Reference:** [EU PEF EF 4.0](https://eplca.jrc.ec.europa.eu)

---

## 1. Overview
The **Induced Pollution Index (IPI)** is a single-score aggregation of the 16 environmental impact categories defined by the European Commission's Product Environmental Footprint (PEF) methodology. The algorithm normalizes these diverse impacts (CO2, m3 of water, kg of waste) into a **unitless index** where **100** represents the neutral market benchmark.

---

## 2. The Multi-Criteria Formula
The final IPI score ($S_{IPI}$) is calculated by summing the weighted and normalized results of the 16 impact categories ($i$):

$$S_{IPI} = \sum_{i=1}^{16} (E_i \times N_i \times W_i) \times C_{DQR}$$

### Variables:
*   **$E_i$ (Environmental Impact):** The raw value of the impact category $i$ (e.g., kg CO2 equivalent).
*   **$N_i$ (Normalization Factor):** A factor used to scale the impact relative to the global annual impact of an average citizen.
*   **$W_i$ (Weighting Factor):** The official EU weighting for the category (e.g., Climate Change = 21.06%).
*   **$C_{DQR}$ (Data Quality Rating Coefficient):** A penalty or bonus based on the reliability of the data source.

---

## 3. Official Impact Weighting (EF 4.0)
Based on the latest [EU JRC Weighting Factors](https://green-forum.ec.europa.eu), the IPI prioritizes impacts as follows:


| Impact Category | Weight (%) | Unit |
| :--- | :--- | :--- |
| **Climate Change** | 21.06 | kg CO2 eq |
| **Water Use** | 8.51 | m3 world eq |
| **Resource Depletion (Minerals)** | 7.55 | kg Sb eq |
| **Acidification** | 6.05 | mol H+ eq |
| **Fine Particulate Matter** | 8.96 | disease incidence |
| **Human Toxicity (Cancer)** | 2.13 | CTUh |
| **Land Use** | 7.94 | dimensionless (pt) |
| *Other 9 categories...* | *Remaining 37.8%* | - |

---

## 4. The Data Quality Rating (DQR) Penalty
To prevent greenwashing and incentivize the use of **Primary Data** (actual measurements from the factory/service), the algorithm applies a transparency coefficient ($C_{DQR}$):

*   **Verified Primary Data:** $C_{DQR} = 1.0$ (No penalty).
*   **Industry Average Data:** $C_{DQR} = 1.2$ (**+20% Pollution Penalty**).
*   **Unverified/Missing Data:** $C_{DQR} = 1.5$ (**+50% "Default Penalty"**).

*This ensures that a company using coal-based energy but hiding behind "Global Averages" is fiscally penalized compared to an actor proving its solar energy usage on the [EBSI Blockchain](https://ec.europa.eu).*

---

## 5. Benchmarking & Neutrality (The 100-Point Rule)
For every product category (defined by [PEFCR](https://defence-industry-space.ec.europa.eu)), a **Representative Product (RP)** is calculated.

$$IPI = \left( \frac{\text{Actual Score}}{\text{Representative Product Score}} \right) \times 100$$

*   **IPI < 100:** Superior environmental performance (Eligible for **VAT Bonus**).
*   **IPI = 100:** Neutral / Market Average (Standard VAT).
*   **IPI > 100:** Inferior environmental performance (Subject to **VAT Malus**).

---

## 6. Implementation (JSON Input Example)
The IPI engine expects a machine-readable input from the [Digital Product Passport (DPP)](https://commission.europa.eu):

```json
{
  "protocol_version": "1.0.0-beta",
  "product_id": "DPP-EU-123456",
  "impacts": {
    "climate_change": 45.2,
    "water_scarcity": 2.1,
    "resource_minerals": 0.0003
  },
  "data_quality": "verified_primary",
  "ipi_output": 84.2
}