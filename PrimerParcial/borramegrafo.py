import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()



ruta=['2D', '2C', '2B', '3B', '3D', '4D', '4C', '5D', '6D', '7D', '7C', '7B', '8B', '9B', '10B', '10A', '8D', '9D', '10D', '9E', '9F', '9G', '9H', '10H', '11H', '12H', '13H', '14H', '15H', '9I', '7E', '4E', '4F', '5F', '4G', '3G', '2G', '2H', '2I', '3I', '4I', '5I', '6I']


for e in ruta:
  G.add_node(e)  


# G.add_nodes_from([2, 3])

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()