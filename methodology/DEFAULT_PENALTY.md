# ⚠️ Default Penalty: Data Freshness & Non-Compliance
**Protocol Version:** 1.0.0-beta  
**Standard Reference:** [EU PEF Data Quality Rating (DQR) Requirements](https://eplca.jrc.ec.europa.eu)

---

## 1. The Objective: Anti-Stagnation
Environmental performance is dynamic. A factory that was efficient in 2024 may become a laggard by 2026 if it doesn't upgrade its energy mix. The **IPI Protocol** enforces data freshness to ensure that [VAT Modulation](../Fiscal-Models/VAT_MODULATION.md) reflects current reality, not past achievements.

---

## 2. The Expiration Mechanism
Every IPI certification anchored on the [EBSI Blockchain](../Technical-Stack/BLOCKCHAIN_EBSI.md) carries a **Validity Timestamp**.

*   **Standard Cycle:** 12 months from the date of verification.
*   **Warning Phase:** At T-minus 30 days, the [Digital Product Passport (DPP)](../Technical-Stack/DPP_INTEROP.md) triggers an automated alert to the manufacturer's [EU Digital Identity Wallet](https://github.com).

---

## 3. The "Worst-in-Class" Default Penalty
If a product's IPI certification expires or if a manufacturer refuses to provide primary data, the **Default Penalty** is automatically applied.

### 3.1. Calculation Logic
In the current Protocol version (v1.0.0-beta), if an IPI certification expires or data is missing:
*   **The Penalty:** A flat **+50% multiplier (1.5 coefficient)** is applied to the reference benchmark.
*   **Future Roadmap:** Integration of a dynamic "Worst-in-Class" (90th percentile + 15%) model as a PEF repository becomes available in the [EU EF Database](https://eplca.jrc.ec.europa.eu) and PEF declaration becomes mandatory.

### 3.2. Fiscal Consequence
An expired IPI instantly shifts the product into the **highest VAT bracket** defined by the sovereign nation:
*   **Active IPI (65):** 5% VAT (example Bonus).
*   **Expired IPI (Default 150):** 25%+ VAT (example Maximum Malus).

---

## 4. Re-Certification Protocol
To remove the Default Penalty, the actor must:
1.  Submit a new **Primary Data** audit.
2.  Have the data verified by an authorized [CE Marking Notified Body](https://single-market-economy.ec.europa.eu).
3.  Anchor the new **Verifiable Credential** on the blockchain.

---

## 5. Protecting the Integrity of the "Measuring Rod"
The Default Penalty prevents "Data Camping," where an actor relies on an old, favorable score while their actual performance degrades. It ensures a constant **race to the top** by making transparency the path of least fiscal resistance.

---

## 🚀 Future Roadmap: The Dynamic "Worst-in-Class" Penalty
- [ ] **Live Market Scanning:** Implement a data-crawler for verified PEF databases to automatically identify the 90th percentile of pollution for a specific product category, replacing the static 1.5 multiplier with a real-time "Market Malus."

