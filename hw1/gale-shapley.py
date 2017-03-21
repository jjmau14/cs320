import stable_matching_helpers as m
import gale_items as gi
        
def open_file(problem_filename):
    problem_file = open(problem_filename, 'r')
    return problem_file
    
def get_count(problem_file):
    count = 0
    for line in problem_file:
        for word in line.split():
            if ':' in word:
                count += 1
    return count / 2
 
def lists_make(problem_file, count):
    curr = ""
    count = count ** 2
    counter = 0
    men = {}
    women = {}
    for line in problem_file:
        for word in line.split():
            #print(word)
            if counter < count:
                if ':' in word:
                    curr = word[:-1]
                    men[curr] = []
                else:
                    men[curr].append(word)
                    counter += 1
            else:
                if ':' in word:
                    curr = word[:1]
                    women[curr] = []
                else:
                    women[curr].append(word)
                    counter += 1
    return [men, women]

def gale(L, count):
    menList = []
    womenList = []
    
    for m,prefList in L[0].items():
        newPrefList = []
        man = gi.male(m, prefList)
        menList.append(man)
    
    for w,prefList in L[1].items():
        woman = gi.female(w, prefList)
        womenList.append(woman)
    
    pairs = gi.galePairs()
    
    while pairs.getNumPairs() != count:
        for m in menList:
            if not pairs.isPaired_m(m.getName()):
                for w in m.getPrefList():
                    if not pairs.isPaired_m(m.getName()):
                        if not pairs.isPaired(w):
                            pairs.appendPair(m.getName(), w)
                            #print("Paired " + m.getName() + " with " + w)
                            break
                        else: 
                            for women in womenList:
                                if women.getName() == w:
                                    #print(women.getName() + "'s current pair: " + pairs.get_current_partner(women.getName()))
                                    if women.isHigherPriority(m.getName(), pairs.get_current_partner(women.getName())):
                                        #print("was higher priority")
                                        pairs.removePair(pairs.get_current_partner(women.getName()), women.getName())
                                        pairs.appendPair(m.getName(), women.getName())
                                        #print(m.getName() + " paired with " + women.getName())
                                    break
                    else:
                        break
    #pairs.printPairs()
    return pairs
                    
def writeFile(pairs, filename):
    f = open(filename, 'w')
    f.write(pairs.toString())
    f.close()

if __name__ == "__main__":
    import sys
    problem_filename = sys.argv[1]
    count = get_count(open_file(problem_filename))
    L = lists_make(open_file(problem_filename), count)
    #print(L)
    solution_filename = problem_filename + '_solution'
    writeFile(gale(L, count), solution_filename)
    