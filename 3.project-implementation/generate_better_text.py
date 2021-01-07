# coding: utf-8
from lib.np import *
from rnnlm_gen import BetterRnnlmGen
from dataset import ptb


corpus, word_to_id, id_to_word = ptb.load_data('train')
vocab_size = len(word_to_id)
corpus_size = len(corpus)


model = BetterRnnlmGen(vocab_size=30223)
#model = BetterRnnlmGen(vocab_size=440)
model.load_params('./BetterRnnlm.pkl')

# Set up start words and skip words
start_words = 'the meaning of life is'
start_ids = [word_to_id[w] for w in start_words.split(' ')]
skip_words = ['N', '<unk>', '$'] 
skip_ids = [word_to_id[w] for w in skip_words]

for x in start_ids[:-1]:
    x = np.array(x).reshape(1, 1)
    model.predict(x)

word_ids = model.generate(start_ids[-1], skip_ids)
word_ids = start_ids[:-1] + word_ids
txt = ' '.join([id_to_word[i] for i in word_ids])
txt = txt.replace(' <eos>', '.\n')
print('-' * 50)
print(txt)