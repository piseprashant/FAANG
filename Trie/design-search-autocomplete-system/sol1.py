class Trie:
  def __init__(self):
    self.root = {}

  def insert(self, sentence):
    cur = self.root
    for letter in sentence:
      if letter not in cur:
        cur[letter] = {}
      cur = cur[letter]

    cur['#'] = sentence

  def search(self , prefix, cur = None):
    if not cur :
      cur = self.root

    for char in prefix:
      if char not in cur:
        return []
      cur = cur[char]

    ans = []

    for k in cur:
      if k == '#':
        ans.append(cur[k])
      else:
        ans += self.search('', cur[k])

    return ans




class AutoComplete(object):
  def __init__(self, sentences, times):
    #print(sentences)
    self.lookup = {}

    for i, s in enumerate(sentences):
      self.lookup[s] = times[i]

    self.trie = Trie()

    for s in sentences:
      self.trie.insert(s)

    self.keyword = ""

  def input(self, c):
    if c == '#' :
      self.lookup[self.keyword] = self.lookup.get(self.keyword, 0) + 1
      self.trie.insert(self.keyword)
      self.keyword = ""
      return []
    else:
      self.keyword += c
      lst = self.trie.search(self. keyword)
      lst.sort(key = lambda x : (-self.lookup[x], x))
      return lst[:3]


#AutoComplete obj = new
times = [5,3,2,2]
obj = AutoComplete(["i love you", "island", "ironman", " i love leetcode"], times)

c = "i"
param = obj.input(c)

print(param)