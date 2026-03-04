# ⚖️ Fiscal Model: Revenue Neutrality (Bonus-Malus)
**Objective:** Transforming VAT into a Dynamic Incentive without Budgetary Deficit.
**Standard Reference:** [EU VAT Directive Modernization 2026](https://taxation-customs.ec.europa.eu)

---

## 1. The Core Principle: The Balanced Scale
The **IPI-based VAT system** is designed to be **revenue-neutral** for the sovereign state. It does not increase the total tax collection; it reallocates the tax burden from low-pollution products (Bonus) to high-pollution products (Malus).

*   **The Malus Revenue:** Collected from products with an **IPI > 100** (High Impact).
*   **The Bonus Subsidy:** Used to lower the price of products with an **IPI < 100** (Low Impact).

---

## 2. Mathematical Balancing Formula
To ensure the national budget remains stable ($ΔR = 0$), the total tax revenue ($R$) must satisfy the following equilibrium:

$$\sum (Sales_{i} \times Price_{i} \times VAT_{standard}) = \sum (Sales_{i} \times Price_{i} \times VAT_{modulated(IPI)})$$

### Variable Adjustment (The Taxation Bins)
Each government sets its own **Taxation Bins** to determine how aggressively the IPI affects the VAT rate.  
To manage tax revenue, government can either vary their bins or their thresholds at their own will. For example:

**State A** applies those bins:
|IPI threshold | VAT rate |
|:---|:---|
|80.0|0.055|
|120.0|0.2|
|1000.0|0.25|

**State B** applies those bins:
|IPI threshold | VAT rate |
|:---|:---|
|30.0|0.0|
|60.0|0.055|
|90.0|0.12|
|120.0|0.2|
|180.0|0.45|
|250.0|0.9|
|1000.0|1.5|

---

## 3. Simulation Example: The Textile Sector

|Product Name              | IPI     | Net (HT)   | Shelf Price State A (Pragmatic)  | Shelf Price State B (Radical) |
|:---|:---|:---|:---|:---|
|Circular-Local T-Shirt    | 0.77 | €25.0 | €26.38 | €25.0 |
|Linear-Global T-Shirt     | 378.53 | €12.0 | €15.0 | €30.0 |


**Result:** The "Gain" from the high-pollution surcharge offsets the "Cost" of the sustainable tax rebate.  
The **market share shifts** toward the lower IPI product.

---

## 4. Addressing Social Justice (Equity Protections)
The protocol naturally induces the **"Localism Dividend":**  
Since local products naturally have lower transport IPIs, they become more affordable for lower-income households compared to high-impact imports.

To prevent the IPI from becoming a "tax on the poor," the protocol recommends:  
**An Exception List:** first necessity high-IPI goods could be set on a *justified* exception list to be renewed periodically.

---

## 5. Anti-Fraud & Real-time Auditing
By linking the [Digital Product Passport (DPP)](https://commission.europa.eu) to the national tax portal via **API**, tax authorities can:
*   Verify the IPI score instantly at the Point of Sale (POS).
*   Prevent "IPI-Dumping" where actors misdeclare scores to gain a lower VAT rate.
*   Automate the tax return process for SMEs using the [EBSI Blockchain](https://ec.europa.eu).
