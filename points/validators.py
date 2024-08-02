from __future__ import annotations

import points.points as points_module


def validate_current_value(current: int) -> None:
    if not isinstance(current, int):
        raise TypeError("Parameter 'current' must be natural number")
    
    if current < 0:
        raise ValueError("Parameter 'current' cannot be less zero")

def validate_maximum_value(maximum: int) -> None:
    if not isinstance(maximum, int):
        raise TypeError("Parameter 'maximum' must be natural number")
    
    elif maximum <= 0:
        raise ValueError("Parameter 'maximum' cannot be less/equal zero")

def validate_may_exceed_value(may_exceed: bool) -> None:
    if not isinstance(may_exceed, bool):
        raise TypeError("Parameter 'may_exceed' must be boolean value")
    
def validate_exceed_logic(
    current: int,
    maximum: int,
    may_exceed: bool
) -> None:
    if maximum < current and not may_exceed:
        raise ValueError(
            "Current value may exceed maximum"
            " if 'may_exceed' has a true value"
        )

def validate_values(current: int, maximum: int, may_exceed: bool) -> None:
    validate_current_value(current)
    validate_maximum_value(maximum)
    validate_may_exceed_value(may_exceed)
    validate_exceed_logic(current, maximum, may_exceed)

def validate_points(points: int | points_module.Points) -> None:
    if not isinstance(points, (int, points_module.Points)):
        raise TypeError("Parameter 'points' must be integer or Points")
    
    elif isinstance(points, int) and points < 0:
        raise ValueError("Parameter points cannot be less than zero")
    
    elif isinstance(points, points_module.Points):
        validate_values(points.current, points.maximum, points.may_exceed)
