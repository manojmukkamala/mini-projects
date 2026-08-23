# second_most_word

Tiny stdlib-only script: find the second-most-repeated word in a
paragraph. If several words tie for second place, it prints them all.

`second_most_word.py` works on a hardcoded sample paragraph: it splits
the text into whitespace tokens, strips leading/trailing `.` and `,`
punctuation, counts occurrences with a plain dict, looks up the second
highest count, and prints the words that have it.

## How to run

No dependencies (pure stdlib), no install needed:

```sh
python3 second_most_word.py
```

## Notes

- Case-sensitive: `This` and `this` count as different words.
- Only `.` and `,` are stripped as punctuation.
- The output is a `dict_keys` view, so tie order is insertion order,
  not alphabetical.
