def find_shortest_path_with_heap(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the heap-based algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """


def find_shortest_path_with_linear_pq(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
                        # init source node distance to 0, other nodes to inf
                        # init a structure to track the previous node for each node
                        # add all nodes to lpq

                        # loop while lpq is not empty:
                        #     current = pop.lpq.lowest

                        #     if current is the target node:
                        #         break
                                
                        #     look at current's vecinos:
                        #         for each vecino:
                        #             new_path_distance =
                        #                 (distance to current) + (edge weight from current to vecino)
                                    
                        #             if(new_path_distance < the vecino's currently recorded distance):
                        #                 vecino's distance=new_path_distance
                        #                 update the vecino's distance in the lpq 
                        #                 record that the vecino's previous node is current # this is to record the path of the node all the way
