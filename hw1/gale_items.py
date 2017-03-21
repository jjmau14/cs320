import stable_matching_helpers as m

class person(object):
    
    def __init__(self, name, prefList):
        self.name = name
        self.prefList = prefList
        
    def getName(self):
        return self.name
    def getPrefList(self):
        return self.prefList
    
class male(person): 
    
    def __init__(self, name, prefList):
        person.__init__(self, name, prefList)

class female(person):
    
    def __init__(self, name, prefList):
        person.__init__(self, name, prefList)

    # returns True if man is higher priority than current man
    def isHigherPriority(self, man1, man2):
        if self.prefList.index(man1) < self.prefList.index(man2):
            return True;
        else:
            return False
    
        
class galePairs:
    def __init__(self):
        self.pairs = {}
        
    def appendPair(self, man, woman):
        self.pairs.update({man:woman})

    def removePair(self, man, woman):
        self.pairs.pop(man, woman)
        
    def getNumPairs(self):
        return len(self.pairs)
    
    def isPaired(self, p):
        return p in self.pairs.values()
    
    def isPaired_m(self, q):
        return q in self.pairs
    
    def printPairs(self):
        for men,women in self.pairs.items():
            print(men, women)
            
    def get_current_partner(self, w):
        d = m.inverse_dict(self.pairs)
        return d[w]
        
    def toString(self):
        retStr = ""
        for men,women in self.pairs.items():
            retStr += (men + " " + women + "\n")
        return retStr