# kanjiquizzer

WHAT THIS PROGRAM DOES:
# Reads from a master file of about 2000 Kanji and their readings
# The file can be found here: http://nihongo.monash.edu/jouyoureadings.html
# User can choose how many terms they want to learn at at time. This learned list only grows as the user calls the
# function more and more.

# Japanese has two phonetic alphabets, Hiragana and Katakana. Each have 46 characters.
# Kanji have either a Onyomi and/or a Kunyomi reading. Onyomi is closer to the original Chinese reading while
# Kunyomi readings are traditional Japanese readings
# Onyomi readings are written in Katakana while Kunyomi readings are in Hiragana
# Romaji is the English characterization of Hiragana/Katakana. Ex: a = あ. It's not always perfect however
# The jaconv module helps normalize all these different readings
