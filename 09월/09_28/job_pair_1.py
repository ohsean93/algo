import sys

sys.stdin = open('input_1.txt', 'r')

def solution(sticker):

    can_cut_max = 0
    cannot_cut_max = 0

    for num in sticker:
        can_cut_max, cannot_cut_max = max(cannot_cut_max, can_cut_max + num), can_cut_max

    return max(can_cut_max, cannot_cut_max)