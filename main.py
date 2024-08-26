from Tasks import BaseChain, TaskParserChain, UserStoryExtractorChain, BacklogPrioritizerChain, SprintPlannerChain
import streamlit as st

from model import ChatGroqClient
import time

class AgileProjectManager:
    def __init__(self, llm):
        self.task_parser = TaskParserChain()
        self.user_story_extractor = UserStoryExtractorChain()
        self.backlog_prioritizer = BacklogPrioritizerChain()
        self.sprint_planner = SprintPlannerChain()

    def process_project(self, project_description):
        retries = 3
        for attempt in range(retries):
            try:
                # Run the chains in sequence
                tasks = self.task_parser.run(project_description)
                user_stories = self.user_story_extractor.run(project_description)
                prioritized_backlog = self.backlog_prioritizer.run(project_description)
                sprint_plan = self.sprint_planner.run(prioritized_backlog)
                return {
                    "tasks": tasks,
                    "user_stories": user_stories,
                    "prioritized_backlog": prioritized_backlog,
                    "sprint_plan": sprint_plan
                }
            except Exception as e:
                if attempt < retries - 1:
                    print(f"Error occurred: {e}. Retrying...")
                    time.sleep(2)  # Wait 2 seconds before retrying
                else:
                    print("Failed after multiple attempts.")
                    raise

def main():
    st.title("Agile Project Manager with LLM")

    # Input field for project description
    project_description = st.text_area("Enter Project Description", height=200)

    # Create the LLM client
    client = ChatGroqClient(api_key="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")
    client.create_client()
    llm = client.get_llm()

    # Process the project when the button is clicked
    if st.button("Generate Agile Artifacts"):
        if project_description.strip() == "":
            st.error("Please enter a project description.")
        else:
            # Initialize AgileProjectManager with the LLM
            project_manager = AgileProjectManager(llm)
            
            retries = 3
            for attempt in range(retries):
                try:
                    # Process the project description
                    result = project_manager.process_project(project_description)

                    # Display the results
                    st.subheader("Tasks")
                    st.write(result["tasks"])

                    st.subheader("User Stories")
                    st.write(result["user_stories"])

                    st.subheader("Prioritized Backlog")
                    st.write(result["prioritized_backlog"])

                    st.subheader("Sprint Plan")
                    st.write(result["sprint_plan"])
                    break
                except Exception as e:
                    if attempt < retries - 1:
                        st.warning(f"Error occurred: {e}. Retrying...")
                        time.sleep(2)
                    else:
                        st.error("Service is currently unavailable. Please try again later.")
                        break

if __name__ == "__main__":
    main()