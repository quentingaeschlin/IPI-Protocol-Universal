# 🧮 Core Algorithm: The IPI Scoring Engine
**Protocol Version:** 1.0.0-beta  
**Standard Reference:** [EU PEF EF 4.0](https://eplca.jrc.ec.europa.eu)

---

## 1. Overview
The **Induced Pollution Index (IPI)** is a single-score aggregation of the 16 environmental impact categories defined by the European Commission's Product Environmental Footprint (PEF) methodology. 

The algorithm normalizes diverse impacts (CO2, m3 of water, disease incidence) into a **unitless index** where **100** represents the neutral market benchmark. This ensures that a T-shirt (Textile) and a Diamond (Mining) can be evaluated on the same fiscal scale, despite their vastly different absolute impacts.

---

## 2. The Mathematical Model: $S_{ipi}$

The calculation implemented in [src/ipi_calculator.py](../src/ipi_calculator.py) follows a standardized ratio-based formula:

$$S_{ipi} = \left( \frac{\sum_{i=1}^{16} (E_i \times W_i)}{FU \times RP_{benchmark}} \right) \times 100 \times f_{dqr}$$

### 🔍 Parameter Breakdown

1. **Total Weighted Impact ($\sum E_i \times W_i$):**
   The sum of all 16 environmental impacts weighted according to the [Official JRC Weighting Factors](https://eplca.jrc.ec.europa.eu).

2. **Functional Unit ($FU$):**
   The "Service Unit" delivered by the product. 
   - *Example (Textile):* Number of wears (Durability factor).
   - *Example (Mining):* Number of carats of polished diamond.
   *Note: This penalizes obsolescence. A lower $FU$ (disposable product) mathematically inflates the final score.*

3. **Representative Product Benchmark ($RP_{benchmark}$):**
   The weighted impact of the sector's "Average Market Product" per unit of service, as defined by the [PEFCR](https://green-forum.ec.europa.eu). 
   - **$S_{ipi} = 100$:** The product matches the market average.
   - **$S_{ipi} < 100$:** Superior environmental performance (Eco-Bonus territory).
   - **$S_{ipi} > 100$:** Inferior environmental performance (Eco-Malus territory).

4. **Data Quality Factor ($f_{dqr}$):**
   A corrective multiplier based on data reliability (DQR):
   - **Verified Primary Data:** $f_{dqr} = 1.0$ (No penalty).
   - **Industry Average Data:** $f_{dqr} = 1.2$ (+20% penalty).
   - **Missing/Expired Data:** $f_{dqr} = 1.5$ (+50% penalty).

---

## 3. Official Impact Weighting (EF 4.0)
Based on the [EU JRC Weighting Factors](https://green-forum.ec.europa.eu), the IPI prioritizes impacts as follows:


| Impact Category | Weight (%) | Unit |
| :--- | :--- | :--- |
| **Climate Change** | 21.06 | kg CO2 eq |
| **Fine Particulate Matter** | 8.96 | disease incidence |
| **Water Use** | 8.51 | m3 world eq |
| **Land Use** | 7.94 | pt (dimensionless) |
| **Resource Depletion (Minerals)** | 7.55 | kg Sb eq |
| **Acidification** | 6.05 | mol H+ eq |
| *Other 10 categories...* | *39.93* | - |

---

## ⚖️ From Science to Fiscality

Once the $S_{ipi}$ is calculated, it is passed to the [VAT Bridge](../src/vat_bridge.py) to trigger a sovereign **Tax Bin**. This bridge converts the environmental score into a final retail price.

### Simulation Example (State B - Radical):


| Calculated $S_{ipi}$ | Performance | Applied VAT Rate |
| :--- | :--- | :--- |
| **< 30** | Elite Circular | **0% (Super-Bonus)** |
| **80 - 120** | Standard Market | **20% (Neutral)** |
| **> 250** | Linear/Disposable | **150% (Prohibitive Malus)** |

---

## 4. Implementation (DPP-Compatible JSON Input Example)
The IPI engine expects a standardized input from the [Digital Product Passport (DPP)](https://commission.europa.eu). 
Below is a simplified representation of an IPI-compliant data packet:

```json
{
  "@context": "https://ipi-protocol.org",
  "product_id": "urn:gs1:21:7612345678901", 
  "protocol_version": "1.0.0-beta",
  "metadata": {
    "rp_benchmark": 0.15,
  },
  "product": {
    "name": "Circular T-Shirt",
    "impacts": { "climate_change": 0.3, "water_use": 0.2 },
    "functional_unit": 80,
    "unit_type": "number_of_wears",
    "dqr_type": "primary"
  }
}

Note on Interoperability: The IPI Protocol uses JSON-LD structures to ensure seamless integration with GS1 Digital Links and the European EBSI Blockchain.