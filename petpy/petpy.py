"""
Petrophysics equations
"""

def gardner (vp, alpha =310, beta = 0.25):
    """
        Commute bulk density (in kg/m3)from vp

    """
    return alpha*vp**beta

def impedance(vp, rho):
    """
    compute impedance
    """
    return vp * rho
