# 🔗 Technical Stack: IPI Inheritance & EBSI Blockchain
**Protocol Version:** 1.0.0-beta  
**Infrastructure:** [European Blockchain Services Infrastructure (EBSI)](https://ec.europa.eu)

---

## 1. The Core Problem: The "Data Silo" Gap
Traditional Life Cycle Assessments (LCA) fail because data is siloed. A manufacturer often doesn't know the *actual* impact of their Tier-3 suppliers. They rely on "generic averages," which hide pollution. 

**The IPI Solution:** Every participant in the supply chain logs their specific impact on a shared, immutable ledger.

---

## 2. The Mechanism: IPI Inheritance (Smart Contracts)
The IPI Protocol uses a **Nested Smart Contract** logic. When a final product is created, it "calls" the IPI scores of its verified components.

### 2.1. The Tokenization of Impact
Each semi-finished good or service is assigned a **Verifiable Credential (VC)** on the EBSI:
*   **Supplier A (Raw Cotton):** Generates an IPI-VC of **40**.
*   **Supplier B (Dyeing Service):** Generates an IPI-VC of **15**.
*   **Manufacturer C (The T-Shirt):** Inherits both, adds its own process IPI (**10**).

**Final Product IPI:** $40 + 15 + 10 = 65$.

### 2.2. Immutable Traceability
If a supplier attempts to "greenwash" their data post-transaction, the [EBSI Ledger](https://digital-strategy.ec.europa.eu) maintains the history. Any discrepancy triggers an automatic **Audit Flag** in the [Digital Product Passport (DPP)](https://commission.europa.eu).

---

## 3. Integration with National Tax Authorities (APIs)
To enable **Smart VAT Modulation**, the blockchain connects directly to the [VAT in the Digital Age (ViDA)](https://taxation-customs.ec.europa.eu) systems.

1.  **Point of Sale (POS):** The retailer scans the product's QR code (DPP).
2.  **API Call:** The system queries the EBSI to verify the IPI's authenticity.
3.  **Real-Time Calculation:** The tax engine applies the **IPI Coefficient** to the standard VAT rate.
4.  **Settlement:** The modulated VAT is recorded, and the "Bonus/Malus" is settled in the national green fund.

---

## 4. Security & Privacy (The "Zero-Knowledge" Approach)
We protect industrial secrets while ensuring transparency:
*   **Public IPI:** The final score is public.
*   **Private Inputs:** The specific supply chain details are encrypted. Only the **Total Aggregated IPI** is visible to the consumer and tax authorities, protecting the manufacturer's competitive recipe.

---

## 5. Why EBSI?
*   **Sovereignty:** It is the official [EU Blockchain infrastructure](https://ec.europa.eu).
*   **Energy Efficiency:** Uses a Proof-of-Authority (PoA) consensus, meaning the blockchain itself has a **near-zero IPI**.
*   **Interoperability:** Designed to communicate with the [Digital Product Passport (DPP)](https://commission.europa.eu) across all 27 Member States.

---
- [ ]  **Action:** Implement the first **Solidity/Rust prototype** for the IPI-Inheritance contract in `/Technical-Stack/contracts/`.