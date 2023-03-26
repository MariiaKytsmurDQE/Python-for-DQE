# input string
text = """homEwork:
tHis iz your homeWork, copy these Text to variable.
You NEED TO normalize it fROM letter CASEs point oF View.also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
it iZ misspeLLing here.fix“iZ” with correct “ is ”, but ONLY when it Iz a mistAKE.
last iz TO calculate nuMber OF Whitespace characteRS in this Text.caREFULL, not only Spaces, but ALL whitespaces.I got 87."""


def normalization(n):
    output = ''
    for x in n.lower().split('\n'):  # Convert string into lower case and split it by '\n'.
        for y in x.split('.'):  # Split again by '.'.
            if y.find('iz') != -1:  # If 'iz' not False.

                y = y.replace(' iz ', ' is ')  # Replace 'iz' with 'is' add space for replacement only where it's needed

            # Creating new punctuation marks.
            if y == '':
                output += '\n'  # Add new '\n'.
            elif y[-1].isalpha():
                output += y.capitalize() + '. '  # Add new '. ' to the end of every sentence.
            elif y[-1].isdigit():
                output += y.capitalize() + '.'  # For last sentence with digit in the end.
            elif y[-1] == ':':
                output += y.capitalize() + '\n'  # For sentence 'Homework'

    return output


# output = normalization(a)


normalized_text = normalization(text)

def creation_of_new_sentence(n):
    last_words_sentence = ''
    last_words = []
    for x in n.lower().split('\n'):  # Convert string into lower case and split it by '\n'
        for y in x.split('.'):  # Split again by '.'
            last_word = [x.replace(':', '') for x in y.split(' ') if x != '' and len(
                y) > 0 and not x.isdigit()]  # Create lists with every word (but not number) of every sentence
            if len(last_word) > 0:  # If list not empty
                last_words.append(last_word[-1])  # Append last word from each sentence to list

        last_words_sentence: str = ' '.join(last_words) + '.'  # Create a new sentence from list 'last_words'

    return last_words_sentence


new_sentence = creation_of_new_sentence(normalized_text)


# Add new sentence to the end of paragraph
def append_new_sentence(n):
    result = normalized_text[:normalized_text.find('paragraph.')+10] \
             + '\n' + new_sentence.capitalize() + normalized_text[normalized_text.find('paragraph.')+10:]
    return result


# Count numbers of whitespaces in the text
def whitespace_count(n):
    whitespaces = normalized_text.count('\n') + normalized_text.count(' ')
    return whitespaces


print(append_new_sentence(new_sentence))
print('Count of all whitespaces:', whitespace_count(normalized_text))
