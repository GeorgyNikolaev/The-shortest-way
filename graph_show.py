from matplotlib.lines import Line2D


def show_graph(ax, vertex, distances, best, start, end, inf=1000000):
    for i in range(len(vertex)-1):
        for j in range(i+1, len(vertex)):
            if distances[i][j] < inf:
                ax.add_line(Line2D((vertex[i][0], vertex[j][0]), (vertex[i][1], vertex[j][1]), color='#aaa'))

    now = start
    for v in best:
        ax.add_line(Line2D((vertex[now][0], vertex[v][0]), (vertex[now][1], vertex[v][1]), color='r'))
        now = v
        if v == end: break

    ax.plot([x[0] for x in vertex], [x[1] for x in vertex], ' ob', markersize=15)






















