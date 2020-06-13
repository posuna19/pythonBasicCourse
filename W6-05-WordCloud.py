import sys

file_contents = '''Nintendo Co., Ltd. is a Japanese consumer electronics and video game company headquartered in Kyoto. The company was founded in 1889 as Nintendo Koppai by craftsman Fusajiro Yamauchi and originally produced handmade hanafuda playing cards. After venturing into various lines of business during the 1960s and acquiring a legal status as a public company under the current company name, Nintendo distributed its first video game console, the Color TV-Game, in 1977. It gained international recognition with the release of the Nintendo Entertainment System in 1985.

Since then, Nintendo has produced some of the most successful consoles in the video game industry, such as the Game Boy, the Super Nintendo Entertainment System, the Wii, and the Nintendo Switch. Nintendo has also developed numerous influential franchises, including Donkey Kong (1981), Mario (1985), The Legend of Zelda (1986), Metroid (1986), Fire Emblem (1990), Star Fox (1993), and Pokémon (1996).

Nintendo has multiple subsidiaries in Japan and abroad, in addition to business partners such as The Pokémon Company and HAL Laboratory. Both the company and its staff have received numerous awards for their achievements, including Emmy Awards for Technology & Engineering, Game Developers Choice Awards and British Academy Games Awards among others. Nintendo is one of the wealthiest and most valuable companies in the Japanese market.'''

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                       "they", "them", \
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                       "been", "being", \
                       "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                       "where", "how", \
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can",
                       "will", "just", "in"]

# LEARNER CODE START HERE
print('*****************')
print(file_contents)
print('*****************')
# Remove puntuaction
clean_content = ''
for character in file_contents:
    if character not in punctuations:
        clean_content += character

print('****** Cleaning ***********')
print(clean_content)
print('*****************')



allWords = clean_content.split()
frequent_words = {}
for word in allWords:
    if word not in uninteresting_words and word.isalpha():
        if word in frequent_words:
            frequent_words[word] += 1
        else:
            frequent_words[word] = 1


print('****** Frecuency of words ***********')
print(frequent_words)

sys.exit(1)