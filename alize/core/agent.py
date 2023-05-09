from langchain import OpenAI
from langchain.chains import ConversationalRetrievalChain
from alize.core.vectordb import VectorDB

class AlizeCore:
    def __init__(self):
        self.chat_hist = []
        self.model = OpenAI()
        self.db = VectorDB()
        self.__init_agent()
    
    def __init_agent(self):
        self.agent = ConversationalRetrievalChain.from_llm(llm=self.model, retriever=self.db.as_retriever())
    
    def update_model(self, model_name):
        self.model = OpenAI(temperature=0, 
                model_name=model_name, 
                verbose=False)
        self.__init_agent()
    
    def update_knowledge(self, keyword):
        self.db.update_knowledge(keyword)
        self.__init_agent()
    
    def predict(self, query):
        input_query = {'question': query, 'chat_history': self.chat_hist}
        result_answer = self.agent(input_query)
        if result_answer is not None:
            qa_tuple = (query, result_answer['answer'])
            self.chat_hist.append(qa_tuple)
        return result_answer['answer']
            
    def reset_chat_hist(self):
        self.chat_hist = []