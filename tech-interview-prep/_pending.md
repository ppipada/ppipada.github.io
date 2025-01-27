---
title: pending stuff
---

# Algos:

permute
combi
views of tree
longest common subsequence
probability mapping to larger sample space
tax slabs
Dijikstras
streams of data

# Questions    

## Q1:
    
input:  words =    ["cat", "bat", "tab"]
        alphabet = ['c', 'b', 'a', 't']
output: True
    

With normal alphabet (a,.. z):
cat, tab, car -> false
abc, dbt, zab -> true


tab, cat, 
O/P: false
    
      words =    ["cat", "cbt", "tab"]
        

def compare(worda, wordb, alphabet):
    
    for c1, c2 in zip(worda, wordb):
        if c1 == c2:
            continue
        for idx, a in enumerate(alphabet):
            if c1 == a:
                for b in alphabet[idx:]:
                    if c2 == b:
                        return True
        return False    
    return False
        
    
def lexico(words, alphabet):
    l = len(words)
    for i in range(l-1):
        c = compare(word[i], word[i+1], alphabet)
        if not c:
            return False
    return True
        
        
    
if __name__ == "__main__":
    words =    ["cat", "bat", "tab"]
    alphabet = ['c', 'b', 'a', 't']
    lexico(words, alphabet)

## Q2:

balance("()") -> "()"
balance("a(b)c)") -> "a(b)c"
balance(")(") -> ""
balance("(((((") -> ""
balance("(()()(") -> "()()"
balance(")(())(") -> "(())"
balance(")())(()()(") -> "()()()"  

balance(")a(") -> "a"
balance(")a()") -> "a()"
balance("()a(") -> "()a"


def brackremove(stri):
    balanced_string = ""
    idxes = []
    stack = []
    for idx, i in enumerate(stri):
        if i == "(":
            stack.push((idx, i))            
        elif i == ")":
            if stack.empty():
                continue
            x = stack.pop()
            if x[1] == "(":
                idxes.append(x[0], x[1])
                idxes.append(idx, i)
                
        else:
            idxes.append(idx, i)
            
    balanced_string += [x[1] for x in sorted(idxes, lambda: key, x[0])]      
    return balanced_string
    
    
if __name__ == "__main__":
    stri = "(a)" 
    brackremove(stri)


## Q3

// "2*3+4" -> 10

// "2*3+4*3" -> 18

def evaluate(strin):
    # array of ints and operations
    # ordering of these oeprations
        # resolve multiplications
        # perform additions
    # eval of these operations.
    
    # arr = [2, MUL, 3, ADD, 4] -> [6, ADD, 4]
    if not strin:
        return 0
    MUL = "MUL"
    ADD = "ADD"
    arr = []
    tmpstr = ""
    for i in strin:
        if i.isnum(str(i)):
            tmpstr += i
        elif i == '*':
            num = str(tmpstr)
            arr.append(num)
            arr.append(MUL) 
        elif i == '+':
            num = str(tmpstr)
            arr.append(num)
            arr.append(ADD)
    if tmpstr:
        num = str(tmpstr)
        arr.append(num)
    
    ## rsolve mul:
    evalindex = 0
    outa = []
    op1 = None
    # 2*3*4+5*6
    for idx in range(arr-1, 3):
        if not op1:
            op1 = arr[idx]
        operation = arr[idx+1]
        op2 = arr[idx+2]
        if operation == MUL:
            res = op1*op2
            op1 = res
        if operation == ADD:
            outa.append(op1)
            op1 = None
            

    # Add
    res = 0
    for i in outa:
        res += i
    
    return res
         
## Q4
   o
  / /
 on2  on3
/ / / /
o o o o
        

class TreeNode():
    self.val = None
    self.right = None
    self.left = None

    \

# n children: 2^level
def insert(root, val):
    if not root:
        return TreeNode()        
    arrnodes = []
    level = [root]
    while level:
        arrnodes.append(level)
        tmplevel = []
        for node in level:
            if node.left:
                tmplevel.append(node.left)
            if node.right:
                tmplevel.append(node.right)
        level = tmplevel
    
    
    arrnodes.append(TreeNode(val))
    

# dfs traversal

# gen_node = (
# if node has 1 child return node.
# if node has 2 chilren, recurse
# if empty children: return None.
)

if gen_node:
    attqach_child()

    # new level
if not gen_node:
    recurse to left most child:
        append.



------------------------------
(abab, ab) = 3
ab.., ..ab, a..b

abb, ab
ab, a.b -> 2
“abcd” == “” -> True

(abacabc, abc) -> (bacbc, bc) + (cbc, bc) + (bc, bc)

a = [0, 2]
b = [1, 4]
c = [3, 5]

0 1 3, 0 1 5, 0 4 5, 2 4 5


def getcount(str1, str2):
    if not str1 and not str2:
         return 1
    if not str1:
         return 0
    if not str2:
         return 1
    
    currentindex = []
    matches = 0
    for i, char in enumerate(str1):
        if str1[i] == str2[0]:
		tmp = getcount(str1[i+1:], str2[1:])
		matches += tmp
    return matches
		


















(abcd, bd) = True
(abcd, be) = False


Requirements: 
if str1 < str2 -> False 
“” == “” -> True
“abcd” == “” -> True
order preserve


def compare(str1, str2):
    if not str1 and not str2:
         return True
    if not str1:
         return False
    if not str2:
         return True
    m = len(str2)
    count = 0
    for i in range(len(str1)):
         if str1[i] == str2[count]:
             count += 1
         if count == m: 
             return True
   
    return False
             
------------------------------



color: R,G,B
shape: diamond, squiggle, oval
number: 1, 2, 3
shading: solid, empty, stripes

card1: 2 red solid diamonds
card1: (1,0,1,2)

set:
(1,0,1,2)
(1,2,0,2)
(1,1,2,1)





I/p: 3 cards
O/p: True/False

boundaries: 

Malformed cards: absent
Same 3 cards: (1,0,1,2) (1,0,1,2) (1,0,1,2) -> true
if len cards < 3 -> false











(1,0,1,2)
(1,2,0,2)
(1,1,2,1)

# card = (x, y, z, w) 
def isset(cards: List): -> bool
    if len(cards) < 3:
        return False
    is_set = False
    for i in range(4):
          same = False
          diff = False
          # same = (cards[0][i] == cards[1][i] == cards[2][i])
          if cards[0][i] == cards[1][i]: 
               same = true
	    else:
               diff = true
          if cards[1][i] == cards[2][i]: 
               if diff:
                   return False
          else:
               if same:
                   return False
	    if cards[0][i] == cards[2][i]: 
               if diff:
                   return False
          else:
               if same:
                   return False

  return True


def findsets(cards: List): -> List

for i in range(len(cards)):
    for j in range(i, len(cards)):
        for k in range(j, len(cards)):
            is =  isset([cards[i], cards[j], cards[k])
            if is:
               return [cards[i], cards[j], cards[k]   
            
return []


--------------------


Please use this Google doc during your interview (your interviewer will see what you write here). To free your hands for typing, we recommend using a headset or speakerphone.

[
["I", "am" , "sam"]
[sam, i, am]
[i, like, green, eggs, and, ham]
]


Requirements: 
I/p: list of list of strings. and another string.

Exactly equal: doesnt matter
if greater then it is out i.e most popular
A word is not found: No prediction
Given whole words



Thinking: 

Per word hash set. Per follow up counters. 
Sorted by count. 

dict {k: {words: count} }


def trainWords(wordlists):  
	outmap = {}
	if not wordlists:
		return outmap
	for sent in wordlists:
		if not sent:
 			continue 	
for idx, w in enumerate(sent):
if w not in outmap:
outmap[w] = {}
if idx + 1 < len(sent):
// increment the counter
if sent[idx+1] not in outmap[w]:
outmap[w][sent[idx+1]] = collections.Counter()
outmap[w][sent[idx+1]] += 1
	return outmap



def searchWord(inword, outmap):
	if (not outmap) or (not inword) or (inword not in outmap):
		return “”
	counters = outmap[inword]
	// w1: 3, w2: 2 
	return maxcount(counters)
 


// I: {
	#allcount: 3 // total
	am: 2,
	sam: 1,
	like: 1 
}


buckets: [(0.5, am), (0.75, sam), (1, like)]

prob = rand.rand(0, 1)

for x, word in buckets:
	if prob < x:
		return word
