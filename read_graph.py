def read_graph(file_str):
    graph = {}
    input = open(file_str, 'r')
    lead = int(input.readline())
    for idx, line in enumerate(input):
        edges = []
        edges_str = line.rstrip('\n').split(' ')
        for e_idx, edge in enumerate(edges_str):
            if edge is not '-':
                edges.append({'id': e_idx, 'weight': float(edge)})
        vertex = {
            'edges': edges
        }
        graph[idx] = vertex;
    input.close()

    return {
        'graph': graph,
        'lead': lead,
    }