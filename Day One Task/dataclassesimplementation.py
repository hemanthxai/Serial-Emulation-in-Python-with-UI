from dataclasses import dataclass
from typing import List
from datetime import date


@dataclass
class Employee:
    name: str
    emp_id: int
    skill_list: List[str]
    date_of_joining: date


def main():

    emp = Employee(
        name="Hemanth",
        emp_id=12345,
        skill_list=["Python", "IoT"],
        date_of_joining=date(2024, 8, 26),
    )


if __name__ == "__main__":
    main()
