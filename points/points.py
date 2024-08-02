from __future__ import annotations

from points.validators import (
    validate_current_value,
    validate_maximum_value,
    validate_may_exceed_value,
    validate_exceed_logic,
    validate_values,
    validate_points
)


class Points:

    def __init__(
        self,
        current: int,
        maximum: int,
        *,
        may_exceed: bool = False
    ) -> None:
        validate_values(current, maximum, may_exceed)
        self._current = current
        self._maximum = maximum
        self._may_exceed = may_exceed

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._current}, {self._maximum})"
    
    def __str__(self) -> str:
        return f"{self._current:04}/{self._maximum:04}"

    def __eq__(self, points: int | Points) -> bool:
        validate_points(points)
        if isinstance(points, int):
            return self._current == points
        
        return self._current == points._current
    
    def __ne__(self, points: int | Points) -> bool:
        return not (self == points)

    def __lt__(self, points: int | Points) -> bool:
        validate_points(points)
        if isinstance(points, int):
            return self._current < points
        
        return self._current < points._current
    
    def __le__(self, points: int | Points) -> bool:
        return self == points or self < points
    
    def __gt__(self, points: int | Points) -> bool:
        validate_points(points)
        if isinstance(points, int):
            return self._current > points
        
        return self._current > points._current
    
    def __ge__(self, points: int | Points) -> bool:
        return self > points or self == points
    
    def __int__(self) -> int:
        return self._current
    
    def __index__(self) -> int:
        return int(self)
    
    def __complex__(self) -> complex:
        return complex(self._current, self._maximum)

    @property
    def current(self) -> int:
        return self._current
    
    @property
    def maximum(self) -> int:
        return self._maximum
    
    @maximum.setter
    def maximum(self, maximum: int) -> None:
        validate_maximum_value(maximum)
        validate_exceed_logic(self._current, maximum, self._may_exceed)
        self._maximum = maximum
    
    @property
    def may_exceed(self) -> bool:
        return self._may_exceed
    
    @may_exceed.setter
    def may_exceed(self, may_exceed: bool) -> None:
        validate_may_exceed_value(may_exceed)
        validate_may_exceed_value(
            current=self._current,
            maximum=self._maximum,
            may_exceed=self._may_exceed
        )
        self._may_exceed = may_exceed

    @property
    def reached_zero(self) -> bool:
        return self._current == 0

    @property
    def reached_maximum(self) -> bool:
        return self._current == self._maximum
    
    @property
    def exceeded_maximum(self) -> bool:
        return self._current > self._maximum

    @property
    def reached_exceded_maximum(self) -> bool:
        return self.reached_maximum or self.exceeded_maximum
