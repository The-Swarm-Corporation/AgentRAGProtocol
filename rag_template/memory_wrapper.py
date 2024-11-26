from abc import ABC, abstractmethod
from swarms import Agent

class MemoryWrapper(ABC):
    @abstractmethod
    def add(self, doc: str):
        pass  # Abstract method for adding an item

    @abstractmethod
    def query(self, query: str):
        pass  # Abstract method for querying items
    
    @abstractmethod
    def delete(self, doc: str):
        pass
    
    
agent = Agent(
    long_term_memory=MemoryWrapper()
)