# decision_logic.py

from datetime import datetime
from src.constants import (
    VS_GLOBAL_MEAN,
    VS_GLOBAL_STD,
    VS_CRITICAL_THRESHOLD,
    VS_DURATION_DAYS
)

def check_spectral_alert(vs_series):
    """
    Checks if the ∇S series exceeds the critical threshold
    for a specified number of consecutive days.

    Args:
        vs_series (list of float): Daily ∇S values.

    Returns:
        dict: Alert status and timestamp.
    """
    consecutive_days = 0
    for value in vs_series:
        if value > VS_CRITICAL_THRESHOLD:
            consecutive_days += 1
            if consecutive_days >= VS_DURATION_DAYS:
                return {
                    "alert": True,
                    "triggered_on": datetime.now().isoformat(),
                    "reason": f"∇S > {VS_CRITICAL_THRESHOLD} for {VS_DURATION_DAYS} consecutive days"
                }
        else:
            consecutive_days = 0

    return {
        "alert": False,
        "triggered_on": None,
        "reason": "No critical threshold breach"
    }
