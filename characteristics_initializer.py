from appliable import *
from appliable_stat import *
from blacklist import *
from sensors import *
from utils import *

# выбираем интеративно по одному управлению.
# уже выбранные вносим в блеклист (центр + накрытое поле с сенс_рад и  ю)
# возвращаем список нескольких NonBinaryUnit-ов основанных на редких событиях
# выбираем по нескольку штук точек для разных удаленностей от центра

def get_characs_for_binary(pic, binary, x,y, blacklist, stat_pics):
    blacklist.add(binary)

    ## nearest
    candidates_anchors = get_coords_for_radius(x, y, search_radius=2)
    bins, probs = get_hist(pic.flatten(), 20)
    sorted_nodes_no_u = eval_unconditional_rareness_sf0(candidates_anchors, bins, probs, prob_threshold=0.2)
    sorted_nodes_u_adapted, informativness = adapt_by_u(sorted_nodes_no_u, binary, stat_pics)
    return sorted_nodes_u_adapted, informativness


def eval_unconditional_rareness_sf0(candidates, bins, probs, prob_threshold):
    # каждому кандидату сопоставляем его бин,
    # а через бин оценку вероятности при данной дискретизации
    return evals, sorted_nodes

def adapt_by_u(sorted_nodes_no_u, binary, stat_pics):
    informativness = evaluate_characteristics(characteristics, binary, stat_pics)
    return sorted_nodes_u_adapted, informativness

def evaluate_characteristics(characteristics, binary, pics):
    res = 0
    for non_binary_h in characteristics:
        res += measure_charactericity(non_binary_h, binary, pics)
    return res


