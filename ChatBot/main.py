from nltk.chat.util import Chat, reflections

my_own_reflections = {
    'go': 'gone',
    'hello' : 'hey there'
}

snipets = [
    ['hi my name is (.*)',['Hello %1']],
    ['(?:hi|hello|holla|hey)', ['hi there', 'hey there', 'hayyy']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']]
]

chat = Chat(snipets, my_own_reflections)
chat.converse()