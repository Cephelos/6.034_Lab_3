# MIT 6.034 Lab 3: Constraint Satisfaction Problems
# Written by 6.034 staff

from constraint_api import *
from test_problems import get_pokemon_problem


#### Part 1: Warmup ############################################################

def has_empty_domains(csp) :
    """Returns True if the problem has one or more empty domains, otherwise False"""

    if [] in csp.domains.values():
        return True
    return False

def check_all_constraints(csp) :
    """Return False if the problem's assigned values violate some constraint,
    otherwise True"""

    for i in csp.domains:
        for j in csp.domains:
            for c in csp.constraints_between(i,j):
                if csp.get_assignment(i) is not None and csp.get_assignment(j) is not None and not c.check(csp.get_assignment(i), csp.get_assignment(j)):

                    return False


    return True



#### Part 2: Depth-First Constraint Solver #####################################

def solve_constraint_dfs(problem) :
    """
    Solves the problem using depth-first search.  Returns a tuple containing:
    1. the solution (a dictionary mapping variables to assigned values)
    2. the number of extensions made (the number of problems popped off the agenda).
    If no solution was found, return None as the first element of the tuple.
    """
    stack = [problem]
    extension_count = 0

    while stack:
        problem = stack.pop(0)
        extension_count += 1
        if has_empty_domains(problem) or not check_all_constraints(problem):
            continue

        if not problem.unassigned_vars:
            return problem.assignments, extension_count

        next_var = problem.pop_next_unassigned_var()

        new_problems = []
        for i in problem.get_domain(next_var):
            new_problem = problem.copy().set_assignment(next_var, i)
            new_problems.append(new_problem)

        stack = new_problems + stack
    return None, extension_count







# QUESTION 1: How many extensions does it take to solve the Pokemon problem
#    with DFS?

# Hint: Use get_pokemon_problem() to get a new copy of the Pokemon problem
#    each time you want to solve it with a different search method.

ANSWER_1 = 20


#### Part 3: Forward Checking ##################################################

def eliminate_from_neighbors(csp, var):
    """
    Eliminates incompatible values from var's neighbors' domains, modifying
    the original csp.  Returns an alphabetically sorted list of the neighboring
    variables whose domains were reduced, with each variable appearing at most
    once.  If no domains were reduced, returns empty list.
    If a domain is reduced to size 0, quits immediately and returns None.
    """
    print(csp, "uno")
    marked = []
    altered = set()

    for n in csp.get_neighbors(var):
        for c in csp.constraints_between(var, n):
            for j in csp.get_domain(n):
                bad_val = True
                for i in csp.get_domain(var):

                    if c.check(i, j):
                        bad_val = False

                if bad_val:
                    marked.append((n, j))
                    altered.add(n)

    for n, j in marked:
        csp.eliminate(n, j)

        if len(csp.get_domain(n)) == 0:
            return None

    print(csp, "dos")
    altered = list(altered)
    altered.sort()
    return altered

# Because names give us power over things (you're free to use this alias)
forward_check = eliminate_from_neighbors

def solve_constraint_forward_checking(problem) :
    """
    Solves the problem using depth-first search with forward checking.
    Same return type as solve_constraint_dfs.
    """
    raise NotImplementedError


# QUESTION 2: How many extensions does it take to solve the Pokemon problem
#    with DFS and forward checking?

ANSWER_2 = None


#### Part 4: Domain Reduction ##################################################

def domain_reduction(csp, queue=None) :
    """
    Uses constraints to reduce domains, propagating the domain reduction
    to all neighbors whose domains are reduced during the process.
    If queue is None, initializes propagation queue by adding all variables in
    their default order. 
    Returns a list of all variables that were dequeued, in the order they
    were removed from the queue.  Variables may appear in the list multiple times.
    If a domain is reduced to size 0, quits immediately and returns None.
    This function modifies the original csp.
    """
    raise NotImplementedError


# QUESTION 3: How many extensions does it take to solve the Pokemon problem
#    with DFS (no forward checking) if you do domain reduction before solving it?

ANSWER_3 = None


def solve_constraint_propagate_reduced_domains(problem) :
    """
    Solves the problem using depth-first search with forward checking and
    propagation through all reduced domains.  Same return type as
    solve_constraint_dfs.
    """
    raise NotImplementedError


# QUESTION 4: How many extensions does it take to solve the Pokemon problem
#    with forward checking and propagation through reduced domains?

ANSWER_4 = None


#### Part 5A: Generic Domain Reduction #########################################

def propagate(enqueue_condition_fn, csp, queue=None) :
    """
    Uses constraints to reduce domains, modifying the original csp.
    Uses enqueue_condition_fn to determine whether to enqueue a variable whose
    domain has been reduced. Same return type as domain_reduction.
    """
    raise NotImplementedError

def condition_domain_reduction(csp, var) :
    """Returns True if var should be enqueued under the all-reduced-domains
    condition, otherwise False"""
    raise NotImplementedError

def condition_singleton(csp, var) :
    """Returns True if var should be enqueued under the singleton-domains
    condition, otherwise False"""
    raise NotImplementedError

def condition_forward_checking(csp, var) :
    """Returns True if var should be enqueued under the forward-checking
    condition, otherwise False"""
    raise NotImplementedError


#### Part 5B: Generic Constraint Solver ########################################

def solve_constraint_generic(problem, enqueue_condition=None) :
    """
    Solves the problem, calling propagate with the specified enqueue
    condition (a function). If enqueue_condition is None, uses DFS only.
    Same return type as solve_constraint_dfs.
    """
    raise NotImplementedError

# QUESTION 5: How many extensions does it take to solve the Pokemon problem
#    with forward checking and propagation through singleton domains? (Don't
#    use domain reduction before solving it.)

ANSWER_5 = None


#### Part 6: Defining Custom Constraints #######################################

def constraint_adjacent(m, n) :
    """Returns True if m and n are adjacent, otherwise False.
    Assume m and n are ints."""
    raise NotImplementedError

def constraint_not_adjacent(m, n) :
    """Returns True if m and n are NOT adjacent, otherwise False.
    Assume m and n are ints."""
    raise NotImplementedError

def all_different(variables) :
    """Returns a list of constraints, with one difference constraint between
    each pair of variables."""
    raise NotImplementedError


#### SURVEY ####################################################################

NAME = "Theodore Calabrese"
COLLABORATORS = ""
HOW_MANY_HOURS_THIS_LAB_TOOK = 8
WHAT_I_FOUND_INTERESTING = 'I like dfs'
WHAT_I_FOUND_BORING = 'Very difficult overall'
SUGGESTIONS = None
