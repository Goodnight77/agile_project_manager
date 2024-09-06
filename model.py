from langchain_groq import ChatGroq



class ChatGroqClient:
    def __init__(self, temperature=0, model="llama-3.1-70b-versatile", api_key=None, verbose=True, max_retries=2):
        self.temperature = temperature
        self.model = model
        self.api_key = api_key
        self.verbose = verbose
        self.max_retries = max_retries
        self.llm = None

    def create_client(self):
        if self.api_key:
            self.llm = ChatGroq(
                temperature=self.temperature,
                model=self.model,
                api_key=self.api_key,
                verbose=self.verbose,
                max_retries=self.max_retries,
            )
        else:
            raise ValueError("API key is required.")

    def get_llm(self):
        if self.llm:
            return self.llm
        else:
            raise ValueError("ChatGroq client has not been created yet.")

# Example usage:
client = ChatGroqClient(api_key="your api key")
client.create_client()
llm = client.get_llm()
