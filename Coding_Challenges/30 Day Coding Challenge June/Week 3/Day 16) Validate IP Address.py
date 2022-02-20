class Solution:
    def validIPAddress(self, IP: str) -> str:
        ipdict = {4: ['IPv4', 4, 255, 10], 6: ['IPv6', 8, 65535, 16]}
        dotind, colonind = IP.find('.'), IP.find(':')
        splitupip = []
        if bool(dotind+1) == bool(colonind+1):
            return 'Neither'
        ipcheck = ipdict[4] if dotind != -1 else ipdict[6]
        splitupip = IP.split('.') if dotind != -1 else IP.split(':')
        if len(splitupip) != ipcheck[1]:
            return 'Neither'
        for x in splitupip:
            try:
                if 0 > int(x, ipcheck[3]) or int(x, ipcheck[3]) > ipcheck[2] or len(x) > 4 or x.find('-') != -1 or (ipcheck[0] == 'IPv4' and x[0] == '0' and len(x) > 1):  # (len(str(int(x, ipcheck[3]))) != len(x)))
                    return 'Neither'
            except Exception as _excpt:
                return 'Neither'
        return ipcheck[0]
