from logger import *
from first_binary import *
from visualiser import *
from data import *

def exp0():
    logger = HtmlLogger("first")
    stat_pics = get_numbers_of_type(3)[50]
    binary, characteristics, informativness = get_binary_and_characs_for_situation(stat_pics)
    visualise_binary_and_characters(binary, characteristics, informativness, logger)
    logger.close()

if __name__ == "__main__":
    exp0()