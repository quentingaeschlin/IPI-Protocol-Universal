"""
IPI Protocol Core Library
Standardizing Environmental Fiscality (PEF to VAT)
"""

from .ipi_calculator import IPICalculator
from .vat_bridge import VATBridge

__version__ = "1.0.0-beta"
__author__ = "Quentin Gaeschlin"

# Expose the main classes for easier access
__all__ = ["IPICalculator", "VATBridge"]
