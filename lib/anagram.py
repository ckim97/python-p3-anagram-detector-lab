# your code goes here!
class Anagram:
    def __init__(self, name):
        self.name = name

    def match(self, list):
        anagrams = []
        name = []
        for char in self.name:
            name.append(char)
        
        sortedName = sorted(name)

        for word in list:
            letters = []
            for char in word:
                letters.append(char)
            sortedLetters = sorted(letters)
            if sortedLetters == sortedName:
                anagrams.append(word)

        return anagrams