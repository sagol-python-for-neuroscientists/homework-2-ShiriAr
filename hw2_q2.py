from collections import namedtuple
from enum import Enum
import itertools

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))



def filter_agents(data): # filters out healthy and dead agents
    filtered_agents = tuple(agent for agent in data if agent.category != Condition.HEALTHY and agent.category != Condition.DEAD)
    return filtered_agents
def batch_agents(data,n): # batches remaining agents in groups of 2
    batched_agents = list(itertools.batched(data, n))
    remainder = len(data) % n
    return batched_agents, remainder
def save_filtered_agents(data,n): # saves healthy and dead agents
    saved_agents = [agent for agent in data if agent.category == Condition.HEALTHY or agent.category == Condition.DEAD]
    return saved_agents
def save_remainder(data,n): # saves remaining agents if there is an uneven number
    remainder = batch_agents(data,n)[1]
    if remainder != 0:
        uneven_agents = [batch_agents(data,n)[0][-1][0]]
        return uneven_agents
    else:
        return []
 

def check_category(agent_tuple): # checks the category of the agents in the tuple
    categories = [agent.category for agent in agent_tuple]
    return (agent_tuple, categories)


# The following functions can be used to modify the agents based on the categories of the input tuple
def sick_cure(input_tuple):
    new_agent = Agent(input_tuple[0][0].name, Condition.HEALTHY)
    new_tuple = (new_agent, input_tuple[0][1])
    return new_tuple
def cure_sick(input_tuple):
    new_agent = Agent(input_tuple[0][1].name, Condition.HEALTHY)
    new_tuple = (input_tuple[0][0], new_agent)
    return new_tuple
def cure_dying(input_tuple):
    new_agent = Agent(input_tuple[0][1].name, Condition.SICK)
    new_tuple = (input_tuple[0][0], new_agent)
    return new_tuple
def dying_cure(input_tuple):
    new_agent = Agent(input_tuple[0][0].name, Condition.SICK)
    new_tuple = (new_agent, input_tuple[0][1])
    return new_tuple
def sick_sick(input_tuple):
    new_agent1, new_agent2 = Agent(input_tuple[0][0].name, Condition.DYING), Agent(input_tuple[0][1].name, Condition.DYING)
    new_tuple = (new_agent1, new_agent2)
    return new_tuple
def cure_cure(input_tuple):
    return input_tuple[0]
def sick_dying(input_tuple):
    if input_tuple[0][0].category == Condition.SICK and input_tuple[0][1].category == Condition.DYING:
        new_agent1, new_agent2 = Agent(input_tuple[0][0].name, Condition.DYING), Agent(input_tuple[0][1].name, Condition.DEAD)
        new_tuple = (new_agent1, new_agent2)
        return new_tuple
    elif input_tuple[0][0].category == Condition.DYING and input_tuple[0][1].category == Condition.SICK:
        new_agent1, new_agent2 = Agent(input_tuple[0][0].name, Condition.DEAD), Agent(input_tuple[0][1].name, Condition.DYING)
        new_tuple = (new_agent1, new_agent2)
        return new_tuple
    


# The following function uses the previous functions to modify the agents based on their categories
def modify_agents(input_tuple):
    if input_tuple[1] == [Condition.SICK, Condition.CURE]:
        new_tuple = sick_cure(input_tuple)
        return new_tuple
    elif input_tuple[1] == [Condition.CURE, Condition.SICK]:
        new_tuple = cure_sick(input_tuple)
        return new_tuple
    elif input_tuple[1] == [Condition.CURE, Condition.DYING]:
        new_tuple = cure_dying(input_tuple)
        return new_tuple
    elif input_tuple[1] == [Condition.DYING, Condition.CURE]:
        new_tuple = dying_cure(input_tuple)
        return new_tuple
    elif input_tuple[1] == [Condition.SICK, Condition.SICK]:
        new_tuple = sick_sick(input_tuple)
        return new_tuple
    elif input_tuple[1] == [Condition.CURE, Condition.CURE]:
        new_tuple = cure_cure(input_tuple)
        return new_tuple
    elif input_tuple[1] == [Condition.SICK, Condition.DYING] or input_tuple[1] == [Condition.DYING, Condition.SICK]:
        new_tuple = sick_dying(input_tuple)
        return new_tuple



# the meetup function combines all the previous functions to modify the agents and combine them into a list
def meetup(agent_list):
    filtered = filter_agents(agent_list)
    batched = batch_agents(filtered, 2)[0]
    saved = save_filtered_agents(agent_list, 2)
    uneven_agents = save_remainder(filtered, 2)
    modified_agents = []
    for agent_tuple in batched:
        modified_agents.append(modify_agents(check_category(agent_tuple)))
    modified_agents = modified_agents + saved + uneven_agents
    all_agents = [agent for agent in modified_agents if agent is not None]
    return all_agents




if __name__ == '__main__':
        # sample data
        data0 = (
            Agent("Adam", Condition.SICK),
            Agent("Cure0", Condition.CURE),
            Agent("Cure1", Condition.CURE),
            Agent("Bob", Condition.HEALTHY),
            Agent("Alice", Condition.DEAD),
            Agent("Charlie", Condition.DYING),
            Agent("Vaccine", Condition.SICK),
            Agent("Darlene", Condition.DYING),
            Agent("Emma", Condition.SICK),
            Agent("Cure2", Condition.CURE),
            Agent("Last", Condition.SICK)
            )
        
        data0_agents = meetup(data0)
        print(f"Question 2 solution: {data0_agents}")



