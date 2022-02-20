class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        return int(math.ceil(math.log(buckets, minutesToTest//minutesToDie + 1)))
