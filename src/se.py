def draw_wstate_tree(svm=None):
    import matplotlib.pyplot as plt
    import networkx as nx
    from networkx.drawing.nx_agraph import write_dot, graphviz_layout

    G = nx.DiGraph()
    
    pos = graphviz_layout(G, prog='dot')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw(G)
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)
    nx.draw_networkx_labels(G, pos, font_size=10)
    plt.show()

draw_wstate_tree()