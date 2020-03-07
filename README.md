# neologist

for now just a markov-chain inventing new words.

Needs a list of a few hundreds words to abstract the probabilities.
Produces a lot of bullshit.

Build using Python 3.8. Should work with every 3.x version, but don't quote me on that.

- Provide a file with a bunch of words, separated by lines.
- Point FILENAME to the word list.
- Set N to the amount you want to generate.
- Set OUTPUT_FILE and set SAVING to True to save the generated words to disk.
- Set MONOVOV (monovovel) to True to make the generator use only one vovel in the word: markov-chain -> markav-chan
