from sortedcontainers import SortedDict
from sys import maxsize
from random import random
from collections import OrderedDict
# 1. Выставляем всем вершинам метки 0 для lead, для остальных inf
# 2. Выбираем непокрытую вершину с наименьшей меткой
# 3. Для всех ее соседей пересчитываем метки
# 4. Как соседей нет считаем вершину покрытой
# 5. Переходим на 2 если есть непокрытые вершины
MAGIC_ZEROS = 4

# Особенности реализации:
# Пути хранятся в словаре labels => [:метка]: [:вершина]
# Словарь с сортировкой
# Ключ словаря '<label>_<id>' таким образом избегаем одинаковых ключей (ограничение словаря) и
# сравниваем даже между одинаковыми лейблами, для

def dejkstra(input):
    (labels, vertices) = init_dejkstra(input)
    while bool(vertices.__len__()):
        v_id = get_min_label(vertices)
        if labels[v_id] == float('inf'): # Если есть недостижимые вершины
            return labels
        edges = get_edges(input, v_id)
        (labels, vertices) = calc_labels(labels, edges, v_id, vertices)
    return labels

def calc_labels(labels, edges, v_id, vertices):
    result_labels = labels

    self_label = labels[v_id]
    for edge in edges:
        target_v = edge['id']
        target_w = edge['weight']
        if labels[target_v] > self_label + target_w:
            vertices.__delitem__(get_dict_key(labels[target_v], target_v))
            vertices.__setitem__(
                get_dict_key(self_label + target_w, target_v),
                target_v
            )
            result_labels[target_v] = self_label + target_w


    return (result_labels, vertices)

def get_edges(input, v_id):
    return input['graph'][v_id]['edges']


def get_min_label(vertices):
    return vertices.popitem(0)[1]


def init_dejkstra(input):
    labels = {}
    graph = input['graph']
    lead = input['lead']
    vertices = SortedDict()
    for idx, vertex in graph.items():
        label = 0 if idx == lead else float('inf')
        labels[idx] = label
        vertices.setdefault(
            get_dict_key(label, idx),
            idx
        )
    return (labels, vertices)

def get_dict_key(value, id):
    v_len = len(str(value))
    v_str = '0' * (MAGIC_ZEROS - v_len) + str(value)
    print('%s_%s' % (v_str, id))
    return '%s_%s' % (v_str, id)