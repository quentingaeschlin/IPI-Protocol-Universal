from typing import List, Dict, Optional

class VATBridge:
    """
    Sovereign Fiscal Engine: Modulates VAT rates using IPI Bins.
    Allows tax authorities to set predictable thresholds for 
    market actors and retailers.
    """

    def __init__(self, bins: Optional[List[Dict[str, float]]] = None):
        """
        Initializes the bridge with a list of fiscal brackets.
        Each bin must contain a 'threshold' (IPI limit) and a 'rate' (VAT decimal).
        """
        # Default Protocol Bins (Internal Reference)
        self.bins = bins or [
            {"threshold": 80.0, "rate": 0.05},    # Sustainable / Circular
            {"threshold": 120.0, "rate": 0.20},   # Standard / Neutral
            {"threshold": float('inf'), "rate": 0.30} # Linear / High-Pollution
        ]
        # Ensure bins are sorted by threshold for sequential evaluation
        self.bins.sort(key=lambda x: x["threshold"])

    def get_vat_by_bin(self, ipi_score: float) -> float:
        """
        Retrieves the fixed VAT rate corresponding to the product's IPI bin.
        Returns the rate of the first bin where ipi_score is lower than threshold.
        """
        for bin_entry in self.bins:
            if ipi_score < bin_entry["threshold"]:
                return bin_entry["rate"]
        
        # Fallback to the highest malus bin
        return self.bins[-1]["rate"]

    def get_final_price(self, price_ht: float, ipi_score: float) -> float:
        """
        Calculates the final retail price including IPI-modulated VAT.
        Essential for POS (Point of Sale) and E-commerce integrations.
        """
        vat_rate = self.get_vat_by_bin(ipi_score)
        final_price = price_ht * (1 + vat_rate)
        
        return round(final_price, 2)