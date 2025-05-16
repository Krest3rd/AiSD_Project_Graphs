import sys
from generate import generate_adj_matrix, matrix_to_edge_table, matrix_to_succesor_lists
from adj_matrix import print_matrix, edge_exists_matrix, matrix_BreathFirstSearch, matrix_DepthFirstSearch, matrix_Kahn_topological_sort, matrix_Tarjan_topological_sort,matrix_export
from edge_table import edge_table_print, edge_exists_table, table_BreathFirstSearch, table_DepthFirstSearch, table_Kahn_topological_sort, table_Tarjan_topological_sort, table_export
from succesor_lists import succesor_lists_print, edge_exists_list, list_BreathFirstSearch, list_DepthFirstSearch, list_Kahn_topological_sort, list_Tarjan_topological_sort, list_export
from user_provided import input_to_successor_list, succesor_lists_to_adj_matrix, successor_list_to_edge_table

def help_tip(tip='menu',line='',nodes=1):
    if tip=='menu':
        print("""
================================================
Available actions(case insensitive): 
              
    Back-   Go back to graph's represantation
            choice.
    Bfs -   Breadth First Search from a speci-
            fied node.
    Dfs-    Depth First Search from a specified 
            node.
    Exit-   Exit the program.
    Find -  Find a path between two nodes.
    Help-   Print help.
    Kahn -  Topological Sort with Kahn's 
            Alghoritm .
    Print - Print the graph in prechosen 
            method.
    Tarjan- Topological sort with Tarjan's
            Alghoritm.
    Export- Export the graph in into LaTeX format.

================================================""")

    elif tip=='nodes':
        print("""
================================================
                   Help tip:
    Nodes and (in --generated mode) saturation 
    are required to be a natural number. Nodes 
    are expected to be over 0 while saturation 
    is meant to be between 0 and 100.           
================================================         
              """)
    elif tip=='noderange':
            print(f"Error: Node '{line}' is required to represent a valid node number (1-{nodes})")
    elif tip=='successors':
            print("""
================================================
                   Help tip:
    Successors are nodes with a connection 
    from a specified node. Thus if there's an
    'arrow' from 1 to 2 and 3 then 2 and 3 are 
    successors of 1. You'd enter this data like
    this:
    1> 2 3
    Value of a succsesor must be a natural number
    and must be in range of nodes.
    If there are no successors, leave the space blank.       
================================================  
            """)
#Function validating whether given node is in nodes' range
def validate_node_input(nodes,prompt,value=None):
    if value is None:
        value=input(f"{prompt}> ")
    try:
        node=int(value)
        if node <1 or node > nodes:
            help_tip("noderange",f"{prompt}",nodes)
            return None
        return node
    except ValueError:
        help_tip("noderange",f"{prompt}",nodes)
        return None

def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py --generate | --user-provided")
        sys.exit(1)
    
    mode = sys.argv[1]
    if mode not in ['--generate', '--user-provided']:
        print("Invalid mode. Use --generate or --user-provided")
        sys.exit(1)
    
    #Validation of --genereate
    try:
        if mode == '--generate':
            print("Generating graph...")
            while True:
                try:
                    nodes=int(input("nodes> "))
                    if nodes <=0:
                        raise ValueError("Node count must be positive.")
                    saturation=(int(input("saturation> ")))
                    if saturation < 0 or saturation > 100:
                        raise ValueError("Saturation must be between 0 and 100.")         
                    matrix = generate_adj_matrix(nodes, saturation)
                    edge_table = matrix_to_edge_table(matrix)
                    successor_lists = matrix_to_succesor_lists(matrix)
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")
                    help_tip('nodes')
                    continue  
        else:
            print("Enter graph data manually...")
            while True:
                try:
                    nodes = int(input("nodes> "))
                    if nodes <= 0:
                        raise ValueError("Node count must be positive")
                    break
                except ValueError as e:
                    print(f"Invalid input:{e}")
                    help_tip('nodes')
                    continue 
            
            print("Enter successors for each node (space-separated):")
            try:
                successor_lists = input_to_successor_list(nodes)
                matrix = succesor_lists_to_adj_matrix(successor_lists)
                edge_table = successor_list_to_edge_table(successor_lists)
            except ValueError:
                print("Given successors either not space-separated or with illegal values")
                help_tip('successors')
                sys.exit(1)
        
        while True:
            print("\nChoose representation (matrix/list/table):")
            representation = input("type> ").strip().lower()

            if representation not in ['matrix', 'list', 'table']:
                print("Invalid representation. Choose 'matrix', 'list' or 'table'")
                continue
            
            while True:
                print("")
                action = input("action> ").strip().lower()
                
                if action == 'back':
                    break
                elif action == 'exit':
                    sys.exit(0)
                
                try:
                    if action == 'print':
                        if representation == 'matrix':
                            print("\nAdjacency Matrix:")
                            print_matrix(matrix)
                        elif representation == 'list':
                            print("\nSuccessor Lists:")
                            succesor_lists_print(successor_lists)
                        else:
                            print("\nEdge Table:")
                            edge_table_print(edge_table)
                    
                    elif action == 'find':
                        start= validate_node_input(nodes,"from")
                        if start is None: continue
                        end=validate_node_input(nodes,"to")
                        if end is None: continue
                        
                        if representation == 'matrix':
                            exists = edge_exists_matrix(matrix, start, end)
                        elif representation == 'list':
                            exists = edge_exists_list(successor_lists, start, end)
                        else:
                            exists = edge_exists_table(edge_table, start, end)
                        
                        print(f"{exists}: edge ({start},{end}) {'exists' if exists else 'does not exist'} in the Graph!")
                    
                    elif action in ['bfs', 'breadth']:
                        start = validate_node_input(nodes,"start")
                        if start is None: continue

                        if representation == 'matrix':
                            result = matrix_BreathFirstSearch(matrix, start)
                        elif representation == 'list':
                            result = list_BreathFirstSearch(successor_lists, start)
                        else:
                            result = table_BreathFirstSearch(edge_table, start)
                        print("BFS result:", " ".join(map(str, result)))
                    
                    elif action in ['dfs','depth']:
                        start = validate_node_input(nodes,"start")
                        if start is None:continue
                        if representation == 'matrix':
                            result = matrix_DepthFirstSearch(matrix, start)
                        elif representation == 'list':
                            result = list_DepthFirstSearch(successor_lists, start)
                        else:
                            result = table_DepthFirstSearch(edge_table, start)
                        print("DFS result:", " ".join(map(str, result)))
                    
                    elif action == 'kahn':
                        try:
                            if representation == 'matrix':
                                result = matrix_Kahn_topological_sort(matrix)
                            elif representation == 'list':
                                result = list_Kahn_topological_sort(successor_lists)
                            else:
                                result = table_Kahn_topological_sort(edge_table)
                            print("Kahn's topological sort:", " ".join(map(str, result)))
                        except ValueError as e:
                            print(f"Error: {e}")
                    elif action == 'tarjan':
                        try:
                            if representation == 'matrix':
                                result = matrix_Tarjan_topological_sort(matrix)
                            elif representation == 'list':
                                result = list_Tarjan_topological_sort(successor_lists)
                            else:
                                result = table_Tarjan_topological_sort(edge_table)
                            print("Tarjan's topological sort:", " ".join(map(str, result)))
                        except ValueError as e:
                            print(f"Error: {e}") 
                    elif action == 'help':
                        help_tip()
                    elif action == 'export':
                        if representation == 'matrix':
                            matrix_export(matrix)
                        elif representation == 'list':
                            list_export(successor_lists)
                        else:
                            table_export(edge_table)
                    else:
                        print("Invalid action. Type 'help' for more commands.")
                
                except ValueError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except EOFError:
        print(f"\nCtrl+D detected. Exiting the program.")
        sys.exit(0)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()