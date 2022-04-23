# return longUrl and return shortUrl would work for encode and decode respectively,
# but is not the point of the challenge.
class Codec:

    def __init__(self):
        # two-way dictionaries of all encoded urls so far
        self.longUrl_to_idx = {}
        self.idx_to_LongUrl = {}
        # base for shortened url, chosen realistically
        self.shortUrlBase = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:

        # if it has not previously been encoded, do so
        if not (longUrl in self.longUrl_to_idx):
            # no need to store whole shortUrlBase in every entry
            shortUrlIdx = len(self.longUrl_to_idx)
            self.longUrl_to_idx[longUrl] = shortUrlIdx
            # guaranteed no collision between longUrl and shortUrlIdx,
            # as longUrl is guaranteed to be a valid URl, not good design in terms of security though
            self.idx_to_LongUrl[shortUrlIdx] = longUrl

        # return the static shortUrlBase along with the idx corresponding to the long url in the dictionary
        return self.shortUrlBase + str(self.longUrl_to_idx[longUrl])

    def decode(self, shortUrl: str) -> str:
        # extract idx from url
        idx = int(shortUrl[len(self.shortUrlBase):])

        # get long url from dictionary at index
        return self.idx_to_LongUrl[idx]
