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

EXAMPLE_STR = 'examples/20_0.5.txt'

input = read_graph(EXAMPLE_STR)
start_time = time.time()
pathes_s = dejkstra_simple(input)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
pathes = dejkstra(input)
print("--- %s seconds ---" % (time.time() - start_time))
print_pathes(pathes)
print_pathes(pathes_s)

