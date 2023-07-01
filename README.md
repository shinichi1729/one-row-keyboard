## What's this?
Training and accuracy verification of a [Kytea](http://www.phontron.com/kytea/) - based reading prediction model for one row keyboard. The conversion from alphabets and symbols to numbers is determined by the position of the columns on the keyboard.

```txt
{!, q, a, z} => 1,  {“, w, s, x}  => 2
{#, e, d, c} => 3,  {$, r, f, v}  => 4
{%, t, g, b} => 5,  {&, y, h, n}  => 6
{‘, u, j, m} => 7,  {(, I, k, ,}  => 8
{), o, l, .} => 9,  {p, +, /}     => 9
```

```txt  
this is a pen . => 5682 82 1 036 9  # uniquely determined
```

```txt
5682 82 1 036 9 => ???              # inference from context
```

## Installation
### Building from a package
```bash
$ tar -xzf kytea-X.X.X.tar.gz
$ cd kytea-X.X.X
$ ./configure
$ make
$ make install
$ kytea --help  # success!!
```

### Quick start
```bash
$ echo "外国人参政権" | kytea
外国/名詞/がいこく 人/接尾辞/じん 参政/名詞/さんせい 権/接尾辞/けん
```

## Training: click [here](http://www.phontron.com/kytea/train.html) for details.

- Training dataset
    - https://huggingface.co/datasets/snow_simplified_japanese_corpus
    - 50,000 easy english sentences.

Preprocessing the dataset's Excel file to create train.txt for KyTea training.
```txt
train.txt:
8/i 316/can 75/'t 5399/tell 269/who 2899/will 144843/arrive 48425/first 9/.
7166/many 1687192/animals 6143/have 5336/been 332549633/destroyed 56/by 736/men 9/.
...
```

### How to train
    
```bash
$ train-kytea -full data/train.txt -model model/model.dat
```

### How to make inferences
```bash
$ kytea -model model/model.dat -nows < evaluate_input.txt > evaluate_output.txt
```
