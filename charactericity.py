from appliable import *
from appliable_stat import *
import numpy as np

def measure_charactericity_for_non_bin(non_binary_h, binary, stat_pics1, stat_pics2):
    # прикидываем условную и безусловную гистограмму non_binary_h
    uncond_sample = get_unconditional_non_binary_sample(non_binary_h, sample_size=200, pics=stat_pics1)
    cond_sample = get_conditional_non_binary_sample(non_binary_h,
                                                    condition=binary.apply2, sample_size=100, pics=stat_pics1)
    nbins = 20
    probs_uncond, bins = get_hist(uncond_sample, nbins)
    probs_cond, _ = get_hist(cond_sample, nbins)

    # затем начинаем второй этап - замер ошибки предсказания при его семплинге из двух разных гист
    sample_size2 = 250
    ground_true = get_conditional_non_binary_sample(non_binary_h, condition=binary.apply2, sample_size=sample_size2,
                                                    pics=stat_pics2)
    uncond_prediction = sample_from_hist(probs_uncond, bins, sample_size2)
    cond_prediction = sample_from_hist(probs_cond, bins, sample_size2)
    naive_error = count_error_btw_two_samples(ground_true, prediction=uncond_prediction)
    clever_error = count_error_btw_two_samples(ground_true, prediction=cond_prediction)
    return clever_error - naive_error


def sample_from_hist(probs, bins, sample_size):
    bin_ids =list(range(0, len(probs)))
    bins_sample = np.random.choice(bin_ids, sample_size, p=probs)
    sample = []
    for bin_id in bins_sample:
        val = np.random.uniform(bins[bin_id],bins[bin_id+1])
        sample.append(val)
    return sample

def count_error_btw_two_samples(ground_true, prediction):
    res = 0
    for i in range(len(ground_true)):
        res+=(ground_true[i] - prediction[i])**2
    return res/len(ground_true)


def measure_charactericity_for_bin(binary_h, binary, stat_pics):
    pass


def measure_charactericity(characteristic, binary, stat_pics):
    if isinstance(characteristic, BinaryUnit):
        return measure_charactericity_for_bin(characteristic, binary, stat_pics)
    return measure_charactericity_for_bin(characteristic, binary, stat_pics)
