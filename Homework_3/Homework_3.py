# input string
text = """homEwork:
tHis iz your homeWork, copy these Text to variable.
You NEED TO normalize it fROM letter CASEs point oF View.also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
it iZ misspeLLing here.fix“iZ” with correct “ is ”, but ONLY when it Iz a mistAKE.
last iz TO calculate nuMber OF Whitespace characteRS in this Text.caREFULL, not only Spaces, but ALL whitespaces.I got 87."""

normalized_text = ''
last_words = []

for x in text.lower().split('\n'):  # Convert string into lower case and split it by '\n'.
    for y in x.split('.'):  # Split again by '.'.
        if y.find('iz') != -1:  # If 'iz' not False.

            y = y.replace(' iz ', ' is ')  # Replace 'iz' with 'is' add space for replacement only where it's needed.

            # Create list with every word (but not number) of every sentence, including empty (when '/n').
        last_word = [x.replace(':', '') for x in y.split(' ') if x != '' and len(y) > 0 and not x.isdigit()]

        if len(last_word) > 0:  # If list not empty
            last_words.append(last_word[-1])  # Append last word from each sentence to list.

        # Creating new punctuation marks.
        if y == '':
            normalized_text += '\n'  # Add new '\n'.
        elif y[-1].isalpha():
            normalized_text += y.capitalize() + '. '  # Add new '. ' to the end of every sentence.
        elif y[-1].isdigit():
            normalized_text += y.capitalize() + '.'  # For last sentence with digit in the end.
        elif y[-1] == ':':
            normalized_text += y.capitalize() + '\n'  # For sentence 'Homework'

print(last_words)

new_sentence = ' '.join(last_words) + '.'  # Create a new sentence(string) from list 'last_words'

print(new_sentence)

# Add new sentence to the end of paragraph
normalized_text = normalized_text[:normalized_text.find('paragraph.')+11] \
                  + new_sentence.capitalize() + normalized_text[normalized_text.find('paragraph.')+10:]

# Count numbers of whitespaces in the text
whitespace_count = len([c for c in text if c.isspace()])

print('Normalized text with new sentence between paragraphs:', normalized_text)
print('Count of all whitespaces:', whitespace_count)
