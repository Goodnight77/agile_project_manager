from Tasks import BaseChain
from Tasks import TaskParserChain
from Tasks import UserStoryExtractorChain
from Tasks import BacklogPrioritizerChain
from Tasks import SprintPlannerChain

class ProjectManagerModel:
    def __init__(self):
        self.task_parser = TaskParserChain() 
        self.sprint_planner = SprintPlannerChain()  
    def run(self, project_description):
        tasks = self.task_parser.run(project_description)  
        sprint_plan = self.sprint_planner.run(tasks)  
        return sprint_plan
