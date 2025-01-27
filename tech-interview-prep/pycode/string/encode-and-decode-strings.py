from functools import reduce


class Codec(object):
    def encode(self, strs):
        """
        Encodes a list of strings to a single string.

        Algorithm: Length info

        :type strs: List[str]
        :rtype: str
        """
        strs = list(map(lambda x: str(len(x)) + "/" + x, strs))
        return reduce(lambda x, y: x + y, strs, "")  # i.e. "".join(strs)

    def decode(self, s):
        """
        Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            j = s.index("/", i)
            l = int(s[i:j])
            strs.append(s[j + 1:j + 1 + l])
            i = j + 1 + l

        return strs


class CodecMethod2(object):
    def encode(self, strs):
        """
        Encodes a list of strings to a single string.

        Algorithm: Escape

        :type strs: List[str]
        :rtype: str
        """
        strs = list(map(lambda x: x.replace("\n", "\n\n") + "_\n_", strs))
        return reduce(lambda x, y: x + y, strs, "")

    def decode(self, s):
        """
        Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        strs = s.split("_\n_")
        strs = strs[:-1]  # clear the trailing delimiter
        return list(map(lambda x: x.replace("\n\n", "\n"), strs))