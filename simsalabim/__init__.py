"""Top-level package for Simsalabim."""

__author__ = """Simon Klein"""
__email__ = 'simon.klein1@rwth-aachen.de'
__version__ = '0.1.0'

from .classes.classes import Signal
from .dsp import decibel
from .io import excel_loader


__all__ = [
    'Signal',
    'decibel',
    'excel_loader']