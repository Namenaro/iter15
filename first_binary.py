
# создаем первый бинарный  итем и его характеристики
# характеристики это набор управлений h1,..,hn
# они берустя в конкретной ситуации по тем управлениям которые привеи к самым редким результатам
# мы подгоняем их характеричики по ю таким образом, чтоб

from utils import *
from data import *
from sensors import *
from charactericity import *
from blacklist import *
from characteristics_initializer import *
import random

def get_anchor(pic):
    etalon = random.uniform(0, 255)
    helper_unit = BinaryUnit(u_radius=0, sensor_field_radius=0, etalon=etalon, event_diameter=20, dx=0,dy=0)
    XY = apply_binary_unit_to_pic(pic, helper_unit)
    if len(XY)==0:
        return get_anchor(pic)
    index = random.randint(0, len(XY) - 1)
    return XY[index][0], XY[index][1]

def get_binaries_for_test(pic, x, y):
    test_binary_units = []
    test_sensor_field_radiuses = [0]
    test_event_diameters = [30]
    for event_diameter in test_event_diameters:
        for sensor_field_radius in test_sensor_field_radiuses:
            etalon = make_measurement(pic, x, y, sensor_field_radius)
            unit = BinaryUnit(u_radius=0, sensor_field_radius=sensor_field_radius,
                              etalon=etalon, event_diameter=event_diameter, dx=0, dy=0)
            test_binary_units.append(unit)
    return test_binary_units


def get_binary_and_characs_for_situation(stat_pics):
    etalon_pics = etalons_of3()
    etalon_pic = select_random_pic(etalon_pics)
    x,y = get_anchor(etalon_pic)
    test_binary_units = get_binaries_for_test(etalon_pic, x, y)

    res_informativness = None
    res_binary = None
    res_characteristics = None

    for test_binary in test_binary_units:
        characteristics, informativness = get_elementary_characts_around_point(etalon_pic, test_binary, x, y, stat_pics)

        if res_informativness is None:
            res_informativness=informativness
            res_binary=test_binary
            res_characteristics = characteristics

        else:
            if informativness > res_informativness:
                res_informativness = informativness
                res_binary = test_binary
                res_characteristics = characteristics
    return res_binary, res_characteristics, res_informativness



