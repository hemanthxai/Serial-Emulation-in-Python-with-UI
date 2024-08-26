from enum import Enum


class Status(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"


status_pending = Status.PENDING
status_in_progress = Status.IN_PROGRESS


print(status_pending.value)
print(status_in_progress.value)
