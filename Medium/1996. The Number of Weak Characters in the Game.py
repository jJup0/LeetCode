from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """
        O(n * log(n)) / O(1)    time / space complexity
        """
        # sort by attack decreasing; for same attack defense increasing
        properties.sort(key=lambda x: (-x[0], x[1]))
        res = 0
        # highest defense so far
        max_defense = 0
        for _, defense in properties:
            # if has lower defense than any so far (has lower attack than all so but higher defense
            # than all with characters so far with same attack due to sorting) then current
            # character is weak
            if defense < max_defense:
                res += 1
            # otherwise update maximum defense
            else:
                max_defense = defense
        return res

    def numberOfWeakCharacters2(self, properties: List[List[int]]) -> int:
        """
        O(n * log(n)) / O(1)     time / space complexity
        """
        # sort by attack stat first and note (inverse) ranking (higher ranking is higher attack)
        properties.sort(key=lambda x: (x[0], -x[1]))
        for i, character in enumerate(properties):
            character.append(i)

        # sort by defense stat
        properties.sort(key=lambda x: -x[1])
        res = 0
        # track highest attack rating so far
        highest_attack_rating = -1
        for _, _, attack_rating in properties:
            # if attack rating is lower than highest so far (defense is lower due to sorting), then
            # current character is weak
            if attack_rating < highest_attack_rating:
                res += 1
            # otherwise update highest attack rating
            else:
                highest_attack_rating = attack_rating
        return res

    def numberOfWeakCharacters3_cheaky_stolen(self, properties: List[List[int]]) -> int:
        """
        n := len(properties), k := highest (allowed) attack/defense
        O(n + k) / O(k)     time / space complexity
        """

        max_defense_for_attacks = [-1] * 100_002
        for att, defense in properties:
            if defense > max_defense_for_attacks[att]:
                max_defense_for_attacks[att] = defense

        current_max = 0
        for i in range(max_defense_for_attacks.index(-1), 0, -1):
            current_max = max(current_max, max_defense_for_attacks[i])
            max_defense_for_attacks[i] = current_max

        return sum(defense < max_defense_for_attacks[attack + 1] for attack, defense in properties)

    def numberOfWeakCharacters1(self, properties: List[List[int]]) -> int:
        """
        O(n^2) / O(n^2) time /space complexity
        """
        # track set of characters that each character has higher attack and defense for and take
        # intersection
        for i, character in enumerate(properties):
            character.append(i)

        def get_stronger(IDX: int):

            properties.sort(key=lambda x: -x[IDX])
            stronger = [set() for _ in range(len(properties))]
            strong = []
            temp = []
            prev = -1
            for prop in properties:
                if prop[IDX] != prev:
                    prev = prop[IDX]
                    strong.extend(temp)
                    temp.clear()

                stronger[prop[2]].update(strong)
                temp.append(prop[2])

            return stronger

        stronger_att = get_stronger(0)
        stronger_def = get_stronger(1)

        return sum(not a.isdisjoint(d) for a, d in zip(stronger_att, stronger_def))
