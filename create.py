def resizeList(l = list):
  words = l[0].split()
  return words


class WordleList():
  def __init__(self, list):
    self.l = list
  
  def clean(self):
    self.l = resizeList(self.l)
    for x in self.l:
      assert len(x) == 5

  def returnList(self):
    resizeList(self.l)
    return self.l

class WordleDict():
  def __init__():
      d = {}

aWords = ['aback abase abate abbey abbot abhor abide abled abode abort about above abuse abyss acorn acrid actor acute adage adapt adept admin admit adobe adopt adore adorn adult affix afire afoot afoul after again agape agate agent agile aging aglow agony agree ahead aider aisle alarm album alert algae alibi alien align alike alive allay alley allot allow alloy aloft alone along aloof aloud alpha altar alter amass amaze amber amble amend amiss amity among ample amply amuse angel anger angle angry angst anime ankle annex annoy annul anode antic anvil aorta apart aphid aping apnea apple apply apron aptly arbor ardor arena argue arise armor aroma arose array arrow arson artsy ascot ashen aside askew assay asset atoll atone attic audio audit augur aunty avail avert avian avoid await awake award aware awash awful awoke axial axiom axion azure']
words = WordleList(aWords)
print(words.returnList())



# lDict = WordleDict()