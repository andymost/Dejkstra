from sortedcollections import ValueSortedDict
from sys import maxsize
from random import random
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

# WARNING связано через замыкание
v_dict = ValueSortedDict()

def dejkstra(input):
    labels = init_dejkstra(input)
    while bool(v_dict.__len__()):
        v_id = pop_min_label()
        if labels[v_id] == float('inf'): # Если есть недостижимые вершины
            return labels
        edges = get_edges(input, v_id)
        labels = calc_labels(labels, edges, v_id)
    return labels

def calc_labels(labels, edges, v_id):
    result_labels = labels

    self_label = labels[v_id]
    for edge in edges:
        target_v = edge['id']
        target_w = edge['weight']
        if labels[target_v] > self_label + target_w:
            v_dict.__delitem__(target_v)
            v_dict.__setitem__(target_v, self_label + target_w)
            result_labels[target_v] = self_label + target_w


    return result_labels

def get_edges(input, v_id):
    return input['graph'][v_id]['edges']


def pop_min_label():
    (id, _v) = v_dict.popitem(0)
    return id


def init_dejkstra(input):
    labels = {}
    graph = input['graph']
    lead = input['lead']

    for idx, vertex in graph.items():
        label = 0 if idx == lead else float(maxsize)
        labels[idx] = label

    v_dict.update(
        list(labels.items())
    )
    return labels
