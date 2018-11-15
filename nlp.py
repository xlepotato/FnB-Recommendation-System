

import nltk
from nltk.tokenize import word_tokenize
import random
from textblob import TextBlob
from textblob import Word
from nltk.corpus import wordnet



GREETING_KEYWORDS = ("hello", "hi", "greeting", "hey", "whazzup", "sup")

GREETING_RESPONSES = ["hi hi !", "hey !", "*nods*", "good day !", "oh, its you !!", "you talking to me ?", "what do you want from me ?!"]

RECOMMENDATION_HOTWORD = ["provide","show", "give", "want"]


def greeting(sentence, translate):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    cap_greeting_responses = []
    text = TextBlob(sentence)
    sentence = preprocess(text, translate)
    # print(sentence)
    sentence = word_tokenize(sentence)
    for word in sentence:
        # w = Word(word)
        # print(w.spellcheck())
        if word.lower() in GREETING_KEYWORDS:
            for wo in GREETING_RESPONSES:
                cap_greeting_responses.append(wo.capitalize())
            reply = random.choice( cap_greeting_responses)
            return reply
        else:
            return None




def preprocess(text, translate):
    if not translate:
        text = text.correct()
        clean_text = ' '.join(text.words)
    else:
        clean_text = ' '.join(text.words)
    clean_text = clean_text.replace('charcot', 'chatbot')
    clean_text = clean_text.replace('cut', 'cute')
    clean_text = clean_text.replace('iii', 'hi')
    # if clean_text[0] == 'h' and clean_text[1] == 'i':
    #     for letter in clean_text[2:]:
    #         if letter == 'i':
    #             clean_text = clean_text.replace(clean_text, 'hi')

    return clean_text


def find_all_noun_in_sentence(text_tags):
    noun_list = []
    noun = None
    for word, pos in text_tags:
        if pos == 'NN' or pos == 'NNS':  # NN is short for noun, NNS is short for noun_plural
            noun_list.append(word)
    return noun_list


def find_noun(text_tags):
    noun = None
    for word, pos in text_tags:
        if pos == 'NN':  # NN is short for noun
            noun = word
            break
    return noun

def find_noun_plural(text_tags):
    noun_plural = None
    for word, pos in text_tags:
        if pos == 'NNS':  # NN is short for noun
            noun_plural = word
            break
    return noun_plural



def find_verb(text_tags):
    verb = None
    partofspeech = None
    for word, pos in text_tags:
        if pos.startswith('VB'):  # any form of verb
            verb = word
            partofspeech = pos
            break

    return verb, partofspeech



def find_adjective(text_tags):
    adjective = None
    for word, pos in text_tags:
        if pos == 'JJ':  # This is an adjective
            adjective = word
            break

    return adjective



def find_response_pronoun(text_tags):
    response_pronoun = None
    for word, pos in text_tags:
        # Disambiguate pronouns
        if pos == 'PRP' and (word == 'you' or word == 'You'):
            response_pronoun = 'I'
        elif pos == 'PRP' and word == 'I':
            # If the user mentioned themselves, then they will definitely be the pronoun
            response_pronoun = 'You'
        elif pos == 'PRP':
            response_pronoun = word

    return response_pronoun



SELF_VERBS_WITH_NOUN_CAPS_PLURAL = [
    "My last startup totally crushed the {noun} vertical",
    "Were you aware I was a serial entrepreneur in the {noun} sector?",
    "My startup is Uber for {noun}",
    "I really consider myself an expert on {noun}",
]

SELF_VERBS_WITH_NOUN_LOWER = [
    "Yeah and I know a lot about {noun}",
    "My friends always ask me about {noun}",
]

SELF_VERBS_WITH_ADJECTIVE = [
    "I'm personally building the {adjective} Economy",
    "I consider myself to be a {adjective}preneur",
]



def starts_with_vowel(word):
    """Check for pronoun compability -- 'a' vs. 'an'"""
    return True if word[0] in 'aeiou' else False



NONE_RESPONSES = [
    "I have no idea what you've just said",
    "huh ? can you repeat that",
    "please say that again",
    "can you rephrase that ?",
    "I don't understand",
    "Let's talk about something else",
]

COMMENTS_ABOUT_SELF = [
    "You may be right",
    "Do you really think so ?",
    "You don't know what you are talking",
    "We find ways to do it",
    "I take that as a compliment"
]


def respond(ques, translate, lan):
    resp = greeting(ques, translate)

    # return greeting response if ques is greeting
    if resp:
        if (translate):
            resp = native_lang_to_en(resp, lan)
        return resp

    # if not greeting, then determine a suitable response

    if not resp:
        # preprocess question
        text = TextBlob(ques)
        clean_text = preprocess(text, translate)

        # find parts of speech
        text = TextBlob(clean_text)
        print(text)
        text_tags = text.tags
        print(text_tags)

        noun = find_noun(text_tags)
        noun_list = find_all_noun_in_sentence(text_tags)
        verb = find_verb(text_tags)
        print(verb, " verb")
        print(noun_list)
        for noun in noun_list:
            if noun == "service" or noun == "services":  # checks if the noun matches the hotword to the F&B recommendation option display
                #Look for possible synonyms for words in the recommendation hotword list.
                for word in RECOMMENDATION_HOTWORD:
                    synonyms = []
                    for syn in wordnet.synsets(word):
                        for l in syn.lemmas():
                            synonyms.append(l.name())
                    list_of_synonyms = set(synonyms)
                    # if verb matches one of the word in the hotkey, including synoyms, display the service
                    for word in list_of_synonyms:
                        if verb[0] == word:
                            return "True"

        adjective = find_adjective(text_tags)
        response_pronoun = find_response_pronoun(text_tags)

        # comments about bot
        if response_pronoun == 'I' and (noun or adjective):
            if noun:
                if random.choice((True, False)):
                    resp = random.choice(SELF_VERBS_WITH_NOUN_CAPS_PLURAL).format(
                        **{'noun': noun.pluralize().capitalize()})
                    if (translate):
                        resp = native_lang_to_en(resp, lan)
                    return resp
                else:
                    resp = random.choice(SELF_VERBS_WITH_NOUN_LOWER).format(**{'noun': noun})
                    if (translate):
                        resp = native_lang_to_en(resp, lan)
                    return resp
            else:
                resp = random.choice(SELF_VERBS_WITH_ADJECTIVE).format(**{'adjective': adjective})
                if (translate):
                    resp = native_lang_to_en(resp, lan)
                return resp

        # comments about self
        if response_pronoun == 'I' and verb:
            resp = random.choice(COMMENTS_ABOUT_SELF)
            if (translate):
                resp = native_lang_to_en(resp, lan)
            return resp

        # construct own response
        resp = []

        if response_pronoun:
            resp.append(response_pronoun)

            if verb:
                verb_word = verb[0]
                if verb_word in ('be', 'am', 'is', "'m"):
                    if response_pronoun.lower() == 'you':
                        resp.append("aren't really")
                        resp = " ".join(resp)
                        if (translate):
                            resp = native_lang_to_en(resp, lan)
                        return resp
                    else:
                        resp.append(verb_word)
                        resp = " ".join(resp)
                        if (translate):
                            resp = native_lang_to_en(resp, lan)
                        return resp

            if noun:
                if response_pronoun.lower() == "i":
                    prop_noun = "am"
                elif response_pronoun.lower() == "you":
                    prop_noun = "are"
                elif response_pronoun.lower in ("he", "she", "it"):
                    prop_noun = "is"
                elif response_pronoun.lower in ("they", "we"):
                    prop_noun = "are"
                else:
                    prop_noun = "is"
                a_or_an = "an" if starts_with_vowel(noun) else "a"
                resp.append(prop_noun + " " + a_or_an + " " + noun)

                # choose a none response if it does not meet any of the crtieria above
            else:
                resp = random.choice(NONE_RESPONSES)
                if (translate):
                    resp = native_lang_to_en(resp, lan)
                return resp

            resp.append(random.choice(("la", "bro", "lol", "bruh", "")))

            resp = " ".join(resp)

        else:
            resp = "yes, let's talk about something else"
    if (translate):
        resp = native_lang_to_en(resp,lan)
    return resp


# In[13]:

def native_lang_to_en(resp, lan):
    b = TextBlob(resp)
    b = b.translate(from_lang='en', to=lan)
    resp = ' '.join(b.words)
    return resp


def detect_language(question):
    b = TextBlob(question)
    translate = False
    try:
        lan = b.detect_language()
        if lan == 'en':
            pass
        else:
            translate = True
            try:
                b = b.translate(from_lang=lan, to='en')
                question = ' '.join(b.words)
            except Exception:
                pass
    except:
        b = TextBlob(question + "   ")
        lan = b.detect_language()
        if lan == 'en':
            pass
        else:
            translate = True
            b = b.translate(from_lang=lan, to='en')
            question = ' '.join(b.words)
    return question, translate, lan



def chat():
    start = False
    keep_looping = True
    question = input('Type and enter to chat : ')
    f = detect_language(question)
    question = f[0]

    while keep_looping:
        if question == "bye" or question == "see you" or question == "Goodbye":
            keep_looping = False

        else:
            answer = respond(question, f[1], f[2])
            if answer == "True":
                start = True
                break
            else:
                print('bot : ', answer)
                print('')
            question = input('Type and enter to chat : ')
            f = detect_language(question)
            question = f[0]
    else:
        final_resp = "talk to you soonest !"
        if f[1]:
            final_resp = native_lang_to_en(final_resp, f[2])
        print("bot : ", final_resp)
    return start

