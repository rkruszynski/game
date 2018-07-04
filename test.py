import itertools
from pprint import pprint

all_heros = {
    1: [3, 5, 1, 1, 4],
    2: [0, 0, 5, 8, 1],
    3: [5, 5, 4, 0, 0],
    4: [5, 0, 0, 1, 8],
    5: [0, 9, 0, 5, 0],
    6: [5, 0, 0, 1, 8],
    7: [0, 9, 0, 5, 0],
}

# hero_possibilities = set(itertools.combinations(all_heros.keys(), 3))
# skills_possibilities = set(itertools.combinations(range(5), 3))
# hero_first = (list(hero_possibilities)[0])


def skills_combined(all_heros, one_hero):
    skills_together = {}
    all_heros_but_one = list(all_heros.keys())
    all_heros_but_one.remove(one_hero)
    hero_possibilities = set(itertools.combinations(all_heros_but_one, 2))
    for foo in hero_possibilities:
        hero_comb = [one_hero]
        for val in foo:
            hero_comb.append(val)

        hero_comb.sort()
        hero_comb = tuple(hero_comb)

        skills_together[hero_comb] = {}
        sum_skills = [0, 0, 0, 0, 0]

        for hero in hero_comb:
            sum_skills = [sum(pair) for pair in zip(sum_skills, all_heros[hero])]
            for comb in  set(itertools.combinations(range(5), 3)):
                skills_together[hero_comb][comb] = sum(sum_skills[i] for i in comb)

    skills_by_value = []
    for k, v in skills_together.items():
        for kk, vv in v.items():
            skills_by_value.append([vv, k, kk])
    skills_by_value.sort(reverse=True)
    return skills_by_value


pprint(skills_combined(all_heros, 7))



