# word_counter

A Python script that counts how often each word appears in a text file, from most frequent to least.

## How it works

Running the script:
1. Creates `words.txt` with a 4-line sample text (**overwrites it if it exists**)
2. Counts the words
3. Writes the results to `counts.txt`

## How to run

```
python word_counter.py
```

Then open `counts.txt`.

## Example

`words.txt`:

```
The quick brown fox jumps over the lazy dog.
The dog barks, and the fox runs away.
A quick fox is a happy fox, but the dog is not happy.
Python is fun, and python is powerful.
```

`counts.txt`:

```
the: 5
fox: 4
is: 4
dog: 3
quick: 2
and: 2
a: 2
happy: 2
python: 2
brown: 1
jumps: 1
over: 1
lazy: 1
barks: 1
runs: 1
away: 1
but: 1
not: 1
fun: 1
powerful: 1
```

## Notes

- Counting is case-insensitive: `The` and `the` are the same word.
- Punctuation is stripped from the start and end of each word.
- Words with the same count appear in the order they first appear in the text.

## Limitations

- The input file name is fixed to `words.txt`. You can't pass your own file yet.
- `words.txt` is overwritten on every run.
- A word with an apostrophe or hyphen in the middle (`don't`, `well-known`) is counted as one word, exactly as written.
- A standalone punctuation mark (such as ` - `) is counted as an empty "word".