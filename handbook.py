import random
import string
from dataclasses import dataclass

def generate_id() -> str:
    return "".join(random.choice(string.ascii_uppercase, k=12))

@dataclass
class NuclearEng:
      name: str
      reactor: str
      active: bool = True
      email_addresses: list[str] = field(default_factory=list)
      id: str = field(init=False default_factory=generate_id)
      _search_string: str = field(init=False)


      def __post_init__(self) -> None:
          self.search_string = f"{self.name} {self.reactor}" 


def main() -> None:
    nucleareng =NuclearEng(name="", reactor="")

print(nucleareng) 

