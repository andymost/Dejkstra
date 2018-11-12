# 1. Выставляем всем вершинам метки 0 для lead, для остальных inf
# 2. Выбираем непокрытую вершину с наименьшей меткой
# 3. Для всех ее соседей пересчитываем метки
# 4. Как соседей нет считаем вершину покрытой
# 5. Переходим на 2 если есть непокрытые вершины

# Особенности реализации:
# Пути хранятся в словаре labels => [:вершина]: [:метка]
# Непосещенные вершины хранятся в массиве vertices по id вершин
# Поиск наименьшей вершины происходит обходом непосещенных вершин и получением значения для них их labels (O(1))

def dejkstra_simple(input):
    (labels, vertices) = init_dejkstra(input)
    while bool(vertices):
        v_id = get_min_label(labels, vertices)
        if (v_id == -1): # Если есть недостижимые вершины
            return labels
        edges = get_edges(input, v_id)
        labels = calc_labels(labels, edges, v_id)
        vertices = remove_vertex(vertices, v_id)
    return labels

def remove_vertex(vertices, v_id):
    idx = vertices.index(v_id)
    return vertices[0:idx] + vertices[idx+1:]

def calc_labels(labels, edges, v_id):
    result = labels
    self_label = labels[v_id]
    for edge in edges:
        target_v = edge['id']
        target_w = edge['weight']
        if labels[target_v] > self_label + target_w:
            result[target_v] = self_label + target_w
    return result

def get_edges(input, v_id):
    return input['graph'][v_id]['edges']


def get_min_label(labels, vertices):
    v_id = -1
    v_val = float('inf')
    for c_v_id in vertices:
        c_v_val = labels[c_v_id]
        if c_v_val < v_val:
            v_val = c_v_val
            v_id = c_v_id
    return v_id


def init_dejkstra(input):
    labels = {}
    vertices = []
    graph = input['graph']
    lead = input['lead']
    for idx, vertex in graph.items():
        label = 0 if idx == lead else float('inf')
        labels[idx] = label
        vertices.append(idx)
    return (labels, vertices)
