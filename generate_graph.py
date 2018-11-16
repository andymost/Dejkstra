from random import random

GRAPH_N = 8000
LEAD_VERTEX = 0
EDGE_PROB = 0.5

spaced = lambda char, pos: str(char) if pos == 0 else ' %s' % char
roundedX10 = lambda val: round(val * 10)


EXAMPLE_STR = 'examples/%s_%s.txt' % (GRAPH_N, EDGE_PROB)

out_file = open(EXAMPLE_STR, 'w')
out_file.write('%s\n' % LEAD_VERTEX)

for i in range(GRAPH_N):
    for j in range(GRAPH_N):
        if i == j:
            out_file.write(spaced('-', i))
        else:
            prob = random()
            w = roundedX10(random())
            if prob > EDGE_PROB and w > 1:
                out_file.write(spaced(w, j))
            else:
                out_file.write(spaced('-', j))
    out_file.write('\n')


