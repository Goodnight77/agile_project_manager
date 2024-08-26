from Tasks import BaseChain, TaskParserChain, UserStoryExtractorChain, BacklogPrioritizerChain, SprintPlannerChain

class ProjectManagerModel:
    def __init__(self):
        # Initialize your internal logic here, like chains or LLMs
        self.task_parser = TaskParserChain()  # Hidden logic
        self.sprint_planner = SprintPlannerChain()  # Hidden logic

    def run(self, project_description):
        # This is the method users will call, they only provide input (e.g., project_description)
        tasks = self.task_parser.run(project_description)  # Hidden logic
        sprint_plan = self.sprint_planner.run(tasks)  # Hidden logic

        # You return the final output (e.g., sprint_plan), but users don’t see the code
        return sprint_plan
