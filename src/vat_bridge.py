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
        # Sort once during initialization for performance
        self.bins.sort(key=lambda x: x["threshold"])

    def get_vat_by_bin(self, ipi_score: float) -> float:
        """
        Returns the VAT rate for the given IPI score.
        Finds the correct VAT rate by looking for the highest threshold
        that the IPI score has exceeded.
        """
        for bin_entry in self.bins:
            if ipi_score <= bin_entry["threshold"]:
                return bin_entry["rate"]
        return self.bins[-1]["rate"]  # Fallback to the highest malus bin

    def get_final_price(self, price_ht: float, ipi_score: float) -> float:
        """
        Calculates the final retail price including IPI-modulated VAT.
        Essential for POS (Point of Sale) and E-commerce integrations.
        
        Args:
            price_ht (float): Price before tax (Hors Taxe).
            ipi_score (float): IPI score of the product.
            
        Returns:
            float: Final price after VAT modulation.
        """
        vat_rate = self.get_vat_by_bin(ipi_score)
        final_price = price_ht * (1 + vat_rate)
        return round(final_price, 2)