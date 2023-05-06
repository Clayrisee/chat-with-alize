from alize.common.constant import BaseKnowledges
from langchain.vectorstores import FAISS
from alize.core.search_api import GoogleSearchAPI
from langchain.embeddings.openai import OpenAIEmbeddings

class VectorDB:
    def __init__(self) -> None:
        self.search_engine = GoogleSearchAPI()
        self.db = FAISS.from_texts([""], OpenAIEmbeddings())
        self.__init_db_with_based_knowledges()
    
    def __init_db_with_based_knowledges(self):
        for keyword in BaseKnowledges.LIST_KNOWLEDGES:
            result_search = self.search_engine.search(keyword)
            self.db.add_texts([result_search])
    
    def update_knowledge(self, keyword):
        result_search = self.search_engine.search(keyword)
        self.db.add_texts([result_search])
    
    def as_retriever(self):
        return self.db.as_retriever(search_type="similarity", search_kwargs={"k":2})