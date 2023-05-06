


class AlizeCore:
    def __init__(self):
        self.chat_hist = []
    
    def __init_agent(self):
        # TODO: Init logic agent 
    
    # Example
    # qa = ConversationalRetrievalChain.from_llm(OpenAI(model_name=), retriever)

    # chat_hist = []
    # query = "Please provide Iphone 14 Pro Specification"
    # result = qa({"question": query, "chat_history": chat_hist})
    # print(f"Question: {query}")
    # print(f"Anwer: {result['answer']}")
    # chat_hist =[(query, result["answer"])]
    # query = "give me price of Iphone 14"
    # result = qa({"question": query, "chat_history": chat_hist})
    # print(f"Question: {query}")
    # print(f"Anwer: {result['answer']}")
        pass
    
    def update_knowledge(self, keyword):
        # Update knowledge based on keyword
        # Reinit Agent
        pass
    
    def predict(self, query):
        # TODO: Run query
        # TODO: Then add to chat history
        pass