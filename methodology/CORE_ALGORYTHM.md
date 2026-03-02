# 🧮 Core Algorithm: The IPI Scoring Engine
**Protocol Version:** 1.0.0-beta  
**Standard Reference:** [EU PEF EF 4.0](https://eplca.jrc.ec.europa.eu)

---

## 1. Overview
The **Induced Pollution Index (IPI)** is a single-score aggregation of the 16 environmental impact categories defined by the European Commission's Product Environmental Footprint (PEF) methodology. The algorithm normalizes these diverse impacts (CO2, m3 of water, kg of waste) into a **unitless index** where **100** represents the neutral market benchmark.

---

## 2. The Multi-Criteria Formula
## 🧮 Mathematical Model: $S_{ipi}$

To ensure total transparency and auditability of the **Induced Pollution Index**, the calculation follows a standardized ratio-based formula. This ensures that a T-shirt (Textile) and a Diamond (Mining) can be evaluated on the same fiscal scale, despite their vastly different absolute impacts.

The formula implemented in [src/ipi_calculator.py](../src/ipi_calculator.py) is:

$$S_{ipi} = \left( \frac{\sum_{i=1}^{16} (E_i \times W_i)}{FU \times RP_{benchmark}} \right) \times 100 \times f_{dqr}$$

### 🔍 Parameter Breakdown

1. **Total Weighted Impact ($\sum E_i \times W_i$):**
   The sum of all 16 environmental impacts (Climate Change, Water, Land Use, etc.) weighted according to the [Official JRC Weighting Factors](https://eplca.jrc.ec.europa.eu).

2. **Functional Unit ($FU$):**
   The "Service Unit" delivered by the product. 
   - *Example (Textile):* number of wears (Durability factor).
   - *Example (Mining):* number of carat of polished diamond.
   *Note: This penalizes obsolescence. A lower $FU$ (disposable product) mathematically inflates the final score.*

3. **Representative Product Benchmark ($RP_{benchmark}$):**
   The weighted impact of the sector's "Average Market Product" as defined by the [PEFCR](https://green-forum.ec.europa.eu). 
   - If the product performs exactly like the market average, the ratio is $1.0$, resulting in a base score of **100**.

4. **Data Quality Factor ($f_{dqr}$):**
   A corrective multiplier based on data reliability (DQR):
   - **Primary Data** (Verified): $1.0$ (No penalty).
   - **Secondary Data** (Industry average): $1.2$ (+20% penalty).
   - **Default/Expired Data**: $1.5$ (+50% penalty).
   More info on DQR below.

---

## ⚖️ From Science to Fiscality

Once the $S_{ipi}$ is calculated, it is passed to the [VAT Bridge](../src/vat_bridge.py) to trigger the corresponding **Tax Bin**.

For example:

| Calculated $S_{ipi}$ | Performance | State (Radical) VAT |
| :--- | :--- | :--- |
| **< 30** | Elite Circular | **0% (Super-Bonus)** |
| **80 - 120** | Standard Market | **20% (Neutral)** |
| **> 250** | Linear/Disposable | **150% (Prohibitive Malus)** |


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

## 🚀 Future Roadmap: Live LCA Integration
- [ ] **Dynamic Normalization:** Integrate the [EU JRC EF Database API]( https://eplca.jrc.ec.europa.eu/ ) to update normalization factors ($N_i$) in real-time, ensuring the "Base 100" remains synchronized with global technical progress.
