from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# from latest_ai_development.tools.custom_tool import GenerateImageTool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class LatestAiDevelopment:
    """LatestAiDevelopment crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def prompt_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["prompt_engineer"],
            verbose=True,
            allow_delegation=False,
            max_retries=0,
        )

    # @agent
    # def image_generator(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["image_generator"],
    #         tools=[GenerateImageTool()],
    #         verbose=True,
    #         allow_delegation=False,
    #         max_retries=0
    #     )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def prompt_engineer_task(self) -> Task:
        return Task(
            config=self.tasks_config["prompt_engineer_task"],
        )

    # @task
    # def image_generator_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["image_generator_task"], output_file="report.md"
    #     )

    @crew
    def crew(self) -> Crew:
        """Creates the LatestAiDevelopment crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
