from collections import deque
from typing import TypeAlias

BitMap: TypeAlias = int
Team: TypeAlias = list[int]


class Solution:
    """
    In a project, you have a list of required skills req_skills, and a list of people.
    The ith person people[i] contains a list of skills that the person has.

    Consider a sufficient team: a set of people such that for every required skill in
    req_skills, there is at least one person in the team who has that skill. We can
    represent these teams by the index of each person.
    - For example, team = [0, 1, 3] represents the people with skills people[0],
    people[1], and people[3].

    Return any sufficient team of the smallest possible size, represented by the index of
    each person. You may return the answer in any order.

    It is guaranteed an answer exists.

    Constraints:
    - 1 <= req_skills.length <= 16
    - 1 <= req_skills[i].length <= 16
    - req_skills[i] consists of lowercase English letters.
    - All the strings of req_skills are unique.
    - 1 <= people.length <= 60
    - 0 <= people[i].length <= 16
    - 1 <= people[i][j].length <= 16
    - people[i][j] consists of lowercase English letters.
    - All the strings of people[i] are unique.
    - Every skill in people[i] is a skill in req_skills.
    - It is guaranteed a sufficient team exists.
    """

    def smallestSufficientTeam(
        self, req_skills: list[str], people: list[list[str]]
    ) -> list[int]:
        """
        Preprocess skills to ints, and greedily choose the next skill to be
        fulfilled as the one with the fewest people with that skill.
        O(2^n) / O(2^n) time / space complexity
        """
        # process skill strings into integers first for performance
        skill_ID_lookup = {skill: pos for pos, skill in enumerate(req_skills)}
        # each entry in `skill_possessor_lookup` contains a sert of all people ID
        # which have that skill
        skill_possessor_lookup: list[set[int]] = [set() for _ in req_skills]

        # add people to skill_possessor_lookup
        for person_id, person in enumerate(people):
            for skill in person:
                skill_ID = skill_ID_lookup[skill]
                skill_possessor_lookup[skill_ID].add(person_id)

        queue: deque[tuple[list[set[int]], Team]] = deque(
            [(skill_possessor_lookup, [])]
        )

        while queue:
            prev_remaining_skills, curr_team = queue.popleft()
            # heuristic: always fulfill skill with fewest eligible people remaining
            rarest_skill_possessors = min(prev_remaining_skills, key=len)
            # iterate through each person, choosing them as the next person for the team
            for person_id in rarest_skill_possessors:
                # remove skills that current person has
                remaining_skills = [
                    possessors
                    for possessors in prev_remaining_skills
                    if person_id not in possessors
                ]
                if not remaining_skills:
                    # found fewest people needed
                    return curr_team + [person_id]
                # add remaining skills and current team to queue
                queue.append((remaining_skills, curr_team + [person_id]))

        raise ValueError("Team does not cover skills")

    def smallestSufficientTeam_slow(
        self, req_skills: list[str], people: list[list[str]]
    ) -> list[int]:
        # todo preprocess skill strings to bitmaps integers
        skill_to_int = {skill: i for i, skill in enumerate(req_skills)}
        int_skill_to_bitmap = [1 << i for i in range(len(req_skills))]

        people.sort(key=lambda person: len(person), reverse=True)
        people_bitmap_skills: list[BitMap] = []

        # skills_to_people: dict[int, list[int]] = {i: [] for i in range(len(req_skills))}
        for skills in people:
            person_skills_bitmap = 0
            for skill in skills:
                person_skills_bitmap |= int_skill_to_bitmap[skill_to_int[skill]]
            people_bitmap_skills.append(person_skills_bitmap)

        def choose_team(
            person_idx: int, chosen_team: list[int], skills_remaining: BitMap
        ) -> None:
            nonlocal min_people, best_team

            # covered all skills
            if skills_remaining == 0:
                min_people = len(chosen_team)
                best_team = chosen_team.copy()
                return

            # all people exhausted
            if person_idx == len(people):
                return

            # will not find a better team
            if len(chosen_team) >= min_people - 1:
                return

            # choose current person
            chosen_team.append(person_idx)
            # remove skills needed
            new_skills_remaining = skills_remaining & (
                ~people_bitmap_skills[person_idx]
            )
            if new_skills_remaining != skills_remaining:
                choose_team(person_idx + 1, chosen_team, new_skills_remaining)
            # undo choose person
            chosen_team.pop()

            # do not choose current person
            choose_team(person_idx + 1, chosen_team, skills_remaining)

        min_people = len(people) + 1
        best_team: list[int] = []
        choose_team(0, [], (1 << (len(req_skills))) - 1)
        return best_team


S = Solution()
print(
    S.smallestSufficientTeam(
        ["java", "nodejs", "reactjs"], [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    )
)
