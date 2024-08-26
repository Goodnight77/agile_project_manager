import os

from langchain import PromptTemplate, LLMChain
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from typing import List, Dict

class BaseChain:
    def __init__(self, template):
        self.llm = ChatGroq(
    temperature=0,
    model= "llama-3.1-70b-versatile", #"llama3-70b-8192",
    api_key="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",
    verbose= True,
    max_retries=2,
)
        self.prompt = PromptTemplate(input_variables=["input"], template=template)
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def run(self, input_text):
        return self.chain.run(input_text)
    


class TaskParserChain(BaseChain):
    def __init__(self):
        template = """
        Extract and list all tasks from the following project description:

        {input}

        Tasks:
        """
        super().__init__(template)

class UserStoryExtractorChain(BaseChain):
    def __init__(self):
        template = """
        Given the following project requirement, extract and format user stories:

        {input}

        Please format each user story as:
        "As a [type of user], I want [an action] so that [a benefit/a value]."

        User Stories:
        """
        super().__init__(template)




class BacklogPrioritizerChain(BaseChain):
    def __init__(self):
        template = """
        Prioritize the following backlog items based on business value, effort, and dependencies:

        {input}

        Provide a numbered list of prioritized items with brief explanations:
        """
        super().__init__(template)



class SprintPlannerChain(BaseChain):
    def __init__(self):
        template = """
        Given the following prioritized backlog and team capacity, create a sprint plan:

        Backlog:
        {input}

        Team Capacity: 100 story points

        Provide a sprint plan with selected items and their estimated story points:
        """
        super().__init__(template)