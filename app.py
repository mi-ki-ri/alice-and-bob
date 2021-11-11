from graphviz import Digraph

graph = Digraph(format="png" , comment="相関図")



# ノードを追加
graph.node("node1", label="Bob")
graph.node("node2", label="Alice")

# 辺を追加
graph.attr("edge", color="pink")
graph.edge("node1", "node2", label="Like")
graph.attr("edge", color="blue")
graph.edge("node2", "node1", label="Dislike")
graph.attr("edge", color="black")

u = graph.unflatten(stagger=3)
u.render("digraph")
