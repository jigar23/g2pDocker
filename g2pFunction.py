from g2pImpl import runG2P


def getG2P(word):
    try:
        value = runG2P(['--model', 'model-3', '--word', word])
        return value
    except:
        return None

'''
# Example use case
pron = getG2P('JIGAR')
print(type(pron))

if pron is None:
    print('Error in translation')
else:
    print(pron)
'''
