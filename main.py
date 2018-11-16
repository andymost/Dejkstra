# 1. Считываем граф (вершина старта, матрица смежности)
# 2. Сохраняем в структуру
# 3. Считаем расстояния по Дейкстре
# 4. Выводим

# Структура графа - Куча вершин
#
# Вершина - тупл из (текущая метка, информация о вершине)
# Текущая метка - метка из алгоритма Дейкстры (для вершины а=0, для остальных inf)
# Информация о вершине - список вершин соседей (тупл из номера вершины и расстояния)

# Рассчет расстояний
# 1. Помещаем все вершины в кучу, расставляя метки
# 2. Извлекаем вершину из кучи
# 3. Для каждого соседа:
#   3.1 Если расстояние от вершины до соседа + метка, меньше расстояния из кучи обновить расстояние в куче
# 4. Сохранить расстояния для вершины



from read_graph import read_graph
from dejkstra_simple import dejkstra_simple
from dejkstra import dejkstra
from print_pathes import print_pathes
import time

EXAMPLE_STR = 'examples/8000_0.5.txt'
N_TIMES = 10

input = read_graph(EXAMPLE_STR)
acc_simple = 0.0
acc_heaped = 0.0


i = 0
while i < N_TIMES:
    i = i + 1
    start_time_s = time.time()
    pathes_s = dejkstra_simple(input)
    acc_simple = acc_simple + (time.time() - start_time_s)

    start_time = time.time()
    pathes = dejkstra(input)
    acc_heaped = acc_heaped + (time.time() - start_time)

print('Simple %s' % (acc_simple/N_TIMES))
print('Heaped %s' % (acc_heaped/N_TIMES))


