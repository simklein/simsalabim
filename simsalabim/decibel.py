"""
Decibel
=====

Provides
  1. Basic calculations with levels.

"""
import numpy as np


def dbsum(levels, axis=None):
    """Summation of levels.

    Parameters
    ---------

    Notes
    -----
    .. math:: L_{sum} = 10 \\log_{10}{\\sum_{i=0}^n{10^{L/10}}}
    """

    levels = np.asanyarray(levels)
    return 10.0 * np.log10((10.0**(levels / 10.0)).sum(axis=None))


def dbmean(levels, axis=None):
    """Energetic average of levels.

    Parameters
    ----------
    levels : list, nparray
        Sequence of levels.

    Notes
    -----
    .. math:: L_{mean} = 10 \\log_{10}{\\frac{1}{n}\\sum_{i=0}^n{10^{L/10}}}
    """

    levels = np.asanyarray(levels)
    return 10.0 * np.log10((10.0**(levels / 10.0)).mean(axis=axis))


def dbsub(a, b):
    """Energitally subtract level b from level a.

    Parameters
    ----------
    a : float
        Level.
    b : float
        Level.

    Notes
    -----
    .. math:: L_{a-b} = 10 \\log_{10}{10^{L_a/10}-10^{L_b/10}}
    Energitally subtract b from a.
    """
    a = np.asanyarray(a)
    b = np.asanyarray(b)
    return 10.0 * np.log10(10.0**(a / 10.0) - 10.0**(b / 10.0))


def dbadd(a, b):
    """Energetic addition of levels.

    Parameters
    ----------
    a : float
        Single level or sequence of levels.
    b : float
        Single level or sequence of levels.

    Notes
    -----
    .. math:: L_{a+b} = 10 \\log_{10}{10^{L_b/10}+10^{L_a/10}}
    Energetically adds b to a.
    """
    a = np.asanyarray(a)
    b = np.asanyarray(b)
    return 10.0 * np.log10(10.0**(a / 10.0) + 10.0**(b / 10.0))
