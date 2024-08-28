from Tasks import BaseChain, TaskParserChain, UserStoryExtractorChain, BacklogPrioritizerChain, SprintPlannerChain

class ProjectManagerModel:
    def __init__(self):
        self.task_parser = TaskParserChain() 
        self.sprint_planner = SprintPlannerChain()  
    def run(self, project_description):
        tasks = self.task_parser.run(project_description)  
        sprint_plan = self.sprint_planner.run(tasks)  
        return sprint_plan
