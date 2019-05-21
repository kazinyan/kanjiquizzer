import jaconv
import random

kanji_dict = {}
learned_list = {}

def menu():
    print('p to print out kanji_dict\n'
          'c to clear learned list\n'
          'l to learn new kanji readings/add to learned_list\n'
          't to test from learned_list\n'
          'q to quit')


def dict_kanji_to_hirakata():  # key = kanji. hira/kata = values as a list
    file = open(u'Common Kanji List', encoding='utf-8')
    line = file.readline().rstrip('\n')
    while line:  # building dictionary
        kanji = line.split('\t')  # 0 = kanji, 1 = hira/kata reading
        readings = kanji[1].split(',')  # some kanji have multiple readings
        kanji_dict[kanji[0]] = readings
        line = file.readline().rstrip('\n')
    file.close()


def random_terms():  # random_terms appends to learned_list versus replacing it. Grows as the program runs more
    global learned_list
    terms = int(input('How many terms would you like to learn? #: '))
    dict_kanji_to_hirakata()
    for i in range(0, terms):
        temp_random_pair = random.choice(list(kanji_dict.items()))
        learned_list[temp_random_pair[0]] = temp_random_pair[1]
    print('New Kanji to learn: ')
    for kanji, readings in learned_list.items():
        print('{} = {}'.format(kanji, readings))


def tester():  # only complete function once user correctly identifies all Kanji in learned_list
    mastered = {}
    while mastered != learned_list:
        for i in range(0, len(learned_list)):
            current_card = random.choice(list(learned_list.items()))
            if current_card[0] in mastered.keys():  # choosing only non-mastered Kanji
                continue
            user_answer = input('What does {} read as? Type in Romaji: '.format(current_card[0]))
            # using jaconv module. converting Romaji to Hiragana and Katakana
            hiragana_answer = jaconv.alphabet2kana(u'{}'.format(user_answer))  # takes Romaji --> Hiragana
            katakana_answer = jaconv.hira2kata(u'{}'.format(hiragana_answer))  # takes Hiragana --> Katakana
            if hiragana_answer in current_card[1] or katakana_answer in current_card[1]:  # checking for on/kun readings
                print('Correct!')
                mastered[current_card[0]] = current_card[1]
            else:
                print('Incorrect. This reads as {}'.format(current_card[1]))
    print('Congratulations! You have mastered the learned_list')


if __name__ == '__main__':
    print('Welcome to Kanji quizzer!')
    while True:
        print('-------' * 20)
        i = input('Enter a command (press m for options): ')
        if i == 'p':
            dict_kanji_to_hirakata()
            for kanji, readings in kanji_dict.items():
                print('{} = {}'.format(kanji, readings))
        elif i == 'l':
            random_terms()
        elif i == 'c':
            learned_list = {}
            print('Learned list is cleared')
        elif i == 't':
            if learned_list == {}:
                print('learned_list is currently empty. Please add to learned_list')
            else:
                tester()
        elif i == 'm':
            menu()
        elif i == 'q':
            quit()
        else:
            print('Please enter a valid command')
