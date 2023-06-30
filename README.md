# WHat is [Kytea](http://www.phontron.com/kytea/)?

KyTea (Kyoto Text Analysis Toolkit) is a tool for text analysis, particularly for languages where word segmentation is challenging, such as Japanese and Chinese. It primarily has functions for word segmentation, part-of-speech tagging, and pronunciation estimation.



## How to train
    
```bash
$ train-kytea -full data/train.txt -model model/model.dat
```

## How to make inferences
```bash
$ kytea -model model/model.dat -nows < evaluate_input.txt > evaluate_output.txt
```
