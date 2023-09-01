from evalu import Evaluator
import numpy as np
from plt import *
import sys

fn=sys.argv[0]
fn=fn[:fn.find(".")]

from const import init_range,evaluations


def annealing_search(call,init_temp=100.0,n=evaluations,maximum=init_range):
#def simulated_annealing(initial_solution, initial_temperature, cooling_rate, num_iterations):
    current_solution = np.random.randint(0,maximum)
    current_cost = call(current_solution,None)
    best_solution = current_solution
    best_cost = current_cost
    
    for _ in range(n):
        temperature = init_temp / np.sqrt(1 + _)
        new_solution = current_solution + np.random.uniform(-1, 1) * temperature
        
        new_cost = call(new_solution,best_cost)
        delta_cost = new_cost - current_cost
        
        if delta_cost < 0 or np.random.uniform(0,1) < np.exp(-delta_cost / temperature):
            current_solution = new_solution
            current_cost = new_cost
            
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
    
    return np.round(best_solution)


if __name__=="__main__":
    ev=Evaluator(annealing_search)
    ev.run()
    ev.plot()
    plt.show()
    ev.print_stats()
    
    ev.save(f"results/{fn}.json")
    
    
    
