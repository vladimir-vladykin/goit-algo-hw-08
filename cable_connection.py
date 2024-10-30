import heapq

def main():
    cables_1 = [15, 4, 4, 2, 1]
    calculate_connection_strategy(cables_1)
    print("\n")

    cables_2 = [15, 4, 7, 3, 3, 1, 4]
    calculate_connection_strategy(cables_2)
    print("\n")


def calculate_connection_strategy(cables):
    if len(cables) == 0:
        return
    
    # transform cables list into heap
    min_heap = cables[:]
    heapq.heapify(min_heap)
    print(f"Calculate best connection strategy for heap of cables:\n{min_heap}\n")

    # Connect cables. 
    # We wan't to make it with best cost. 
    # The longest cable we connect - the more expensive connection is.
    # So do connection from smallest to longest cables, to avoid big cumulative effect 

    # init length with first min element
    total_length = heapq.heappop(min_heap)
    total_connection_cost = 0
    step_counter = 0
    
    # go through the rest of cables in heap, from short to long, and connect them one by one
    while len(min_heap) > 0:
        print(f"Step {step_counter + 1}")

        next_min_cable = heapq.heappop(min_heap)
        cost_of_step = total_length + next_min_cable
        total_connection_cost += cost_of_step
        print(f"Adding cable {next_min_cable} to {total_length}, cost of this step is {cost_of_step}")

        total_length += next_min_cable
        print(f"New total length of connected cable is {total_length}, total cost for now is {total_connection_cost}")
        print("\n")

        step_counter += 1

    print(f"Result:\nsteps count: {step_counter},\ntotal lengths of connected cable is {total_length},\ntotal cost of connection is {total_connection_cost}")
    

if __name__ == '__main__':
    main()