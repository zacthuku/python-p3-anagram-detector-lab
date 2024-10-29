# your code goes here!
class Anagram:
    def __init__(self, word):
        #! we want to store the info onto the instance
        #! -> create a attribute for the instance
        self.word = word.lower()

    def match(self, word_list):
        #! we need to sort the letters inside each word
        sorted_given_word = "".join(sorted(self.word))
        #! then compare each word's sorted letters to
        #! the letters contained inside the word attribute of the self instance
        # final_matches = []
        # for word in word_list:
        #     sorted_current_word = "".join(sorted(word))
        #     if sorted_given_word == sorted_current_word:
        #         final_matches.append(word)
        # return final_matches
        #! Refactor into a list comprehension
        return [
            word for word in word_list if sorted_given_word == "".join(sorted(word))
        ]


# hello = Anagram("hello")
# # import ipdb; ipdb.set_trace()
# hello.match(["ohlel", "cat", "test"])
