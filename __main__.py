from chatbot import factretrievers, factretrieverswsystemmessage

def chat(humanQuery):
    return factretrieverswsystemmessage.answerquestion(humanQuery)


continuechat = True
while continuechat:
    humanQuery = input('>>')
    if humanQuery.lower() == "exit":
        continuechat = False
    else:
        result = chat(humanQuery)
        print(result['output'])