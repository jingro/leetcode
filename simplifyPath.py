class Solution(object):
    def simplifyPath(self, path):
        t = path.split('/')
        sta = []
        for i in t:
            if not i or i == '.':
                continue
            elif i == '..':
                if sta:
                    sta.pop()
            else:
                sta.append(i)
        return '/' + '/'.join(sta)
