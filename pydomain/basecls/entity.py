import abc
from typing import cast, Type, TypeVar, List
from .identity import EntityId
from .event import DomainEvent

T = TypeVar('T', bound=EntityId)


class Entity(abc.ABC):
    
    @abc.abstractmethod
    def __init__(self, id: T) -> None:
        self._id = id
        self._suppress_event = False
        self._domain_events: List[DomainEvent] = []
    
    @property
    def id(self) -> T:
        return self._id

    @property
    def domain_events(self) -> List[DomainEvent]:
        return self._domain_events

    def suppress_event(self) -> None:
        self._suppress_event = True

    def unsuppress_event(self) -> None:
        self._suppress_event = False

    def apply_events(self, event: DomainEvent) -> None:
        if self._suppress_event:
            self._domain_events.append(event)

    def __eq__(self, other: object) -> bool:
        if other is None: return False
        # 使用 is 判斷引用是否一致，等同 id(self) == id(other)
        # 判斷引用的記憶體位置，此外因為是可改變狀態，所以不用覆寫 __hash__
        if self is other: return True
        if type(self) != type(other): return False
        other = cast(Entity, other)
        return self.id == other.id
