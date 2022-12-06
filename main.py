import networkx as nx

import serch_
if __name__ == "__main__":
    """
    It is very important to close the first window that pops up in order to display the window for the second case
    """
    G = nx.DiGraph()
    G.add_edge("a", "b", weight=0.1)
    G.add_edge("b", "c", weight=2)
    G.add_edge("c", "d", weight=2)
    G.add_edge("d", "a", weight=0.9)
    G.add_edge("b", "a", weight=0.1)
    G.add_edge("c", "b", weight=2)
    G.add_edge("d", "c", weight=2)
    G.add_edge("a", "d", weight=0.9)
    serch_.serch_negative_cycle(G)
    ### input : G , exepted output : ['a', 'b', 'a']- for example beacuse (a,b)*(b,a) == 0.1 *0.1 < 1
    G2 = nx.DiGraph()
    G2.add_edge("a", "b", weight=1)
    G2.add_edge("b", "c", weight=2)
    G2.add_edge("c", "d", weight=2)
    G2.add_edge("d", "a", weight=3)
    G2.add_edge("b", "a", weight=4)
    G2.add_edge("c", "b", weight=3)
    G2.add_edge("d", "c", weight=5)
    G2.add_edge("a", "d", weight=6)
    serch_.serch_negative_cycle(G2) ## input : G2 , exepted output :there is no negative cycle. beacuse all of the edges are
                                    ## greater then 1 -> eny mul between them is also bigger then 1 .

