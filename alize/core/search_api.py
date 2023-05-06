from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from abc import ABC, abstractmethod

class BaseSearchAPI(ABC):
    
    @abstractmethod
    def init_search_engine(self):
        pass
    
    @abstractmethod
    def search(self, keywords: str) -> str:
        pass

class GoogleSearchAPI(BaseSearchAPI):
    def __init__(self):
        self.engine = self.init_search_engine()
    
    def init_search_engine(self):
        search = GoogleSearchAPIWrapper()
        return Tool(
            name = "Google Search",
            description="Search Google for recent results.",
            func=search.run
        )
    
    def search(self, keywords: str) -> str:
        return self.engine.run(keywords)