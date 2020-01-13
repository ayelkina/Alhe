import xml.dom.minidom as minidom

from networkx import Graph


class NetworkParser:

    sorted_costs = []

    def load_graph_from_txt(self, filename):
        graph = Graph()
        links_list = []
        cost_list = []
        file = open(filename, "r")
        data = file.read().splitlines()
        for link in data:
            n1, n2, distance = link.split(' ')
            links_list.append((n1, n2, float(distance)))
            cost_list.append(float(distance))

        self.sorted_costs = sorted(cost_list)
        graph.add_weighted_edges_from(links_list)
        file.close()
        return graph

    def load_graph_from_xml(self, filename):
        doc = minidom.parse("sndlib-networks-xml/" + filename)
        link_elements = doc.getElementsByTagName("link")

        graph = Graph()
        link_tuples = []
        cost_list = []

        for link in link_elements:
            source = link.getElementsByTagName("source")[0].firstChild.wholeText
            target = link.getElementsByTagName("target")[0].firstChild.wholeText
            cost = float(link
                         .getElementsByTagName("additionalModules")[0]
                         .getElementsByTagName("addModule")[0]
                         .getElementsByTagName("cost")[0]
                         .firstChild.wholeText)

            cost_list.append(cost)
            link_tuples.append((source, target, cost))

        self.sorted_costs = sorted(cost_list)
        graph.add_weighted_edges_from(link_tuples)
        return graph
