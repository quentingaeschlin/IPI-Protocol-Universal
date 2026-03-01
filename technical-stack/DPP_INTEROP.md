# 📲 Technical Stack: DPP Interoperability & Data Schema
**Protocol Version:** 1.0.0-beta  
**Standard Reference:** [EU Digital Product Passport (DPP) Framework 2026](https://commission.europa.eu)

---

## 1. Technical Objective
The **Digital Product Passport (DPP)** acts as the physical-to-digital bridge for the IPI Protocol. This document defines the machine-readable schema required to embed the **IPI Score** into the DPP metadata, allowing real-time fiscal processing by customs and retail systems.

## 2. Data Schema (JSON-LD / W3C Standard)
To ensure global interoperability across the [European Blockchain Services Infrastructure (EBSI)](https://ec.europa.eu), the IPI data is formatted as a **Verifiable Credential (VC)**.

### 2.1. The IPI Metadata Payload
Each product unit must carry the following JSON-LD structure within its DPP:

```json
{
  "@context": [
    "https://www.w3.org",
    "https://protocol-ipi.org"
  ],
  "type": ["VerifiableCredential", "EnvironmentalImpactCredential"],
  "issuer": "did:ebsi:certifier-id-12345",
  "issuanceDate": "2026-03-01T10:00:00Z",
  "credentialSubject": {
    "id": "urn:dpp:eu:product-serial-98765",
    "ipi_score": 84.2,
    "ipi_version": "1.0.0-beta",
    "verification_link": "https://ebsi.europa.eu..."
  },
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "proofPurpose": "assertionMethod",
    "jws": "eyJhbGciOiJSUzI1NiIs..."
  }
}