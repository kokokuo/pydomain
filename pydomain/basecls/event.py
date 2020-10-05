import abc
import uuid
from datetime import datetime
from typing import Optional, cast, TypeVar
from .identity import EntityId

class DomainEvent(abc.ABC):

    @abc.abstractmethod
    def __init__(self, entity_id: EntityId, occurred_date: Optional[datetime] = None):
        self._entity_id = entity_id
        self._event_id = uuid.uuid1()
        self._occurred_date = occurred_date if occurred_date else datetime.utcnow()

    @property
    def entity_id(self) -> EntityId:
        return self._entity_id

    @property
    def event_id(self) -> uuid.UUID:
        return self._event_id

    @property
    def occurred_date(self) -> datetime:
        return self._occurred_date

    def __eq__(self, other: object) -> bool:
        if type(self) != type(other):
            return False
        other = cast(DomainEvent, other)
        return (self.event_id, self.occurred_date) == (other.event_id, other.occurred_date)
