This is the code for work in this [Study of Attention Mechanisms and Adversarial Training for Question Answering]. 

## Getting started
- If your machine doesn't have a GPU, change `tensorflow-gpu==1.4.1` to `tensorflow==1.4.1` in `requirement.txt`.
- Run the startup script `./get_started.sh` to create a conda environment `squad`. This would download the GloVe word embeddings, download and pre-process SQuAD 1.1, SQuAD 2.0 and Adversarial suqad datasets (the AddSent version) and store them all in `data` directory. 
- Activate the created environment `source activate squad`. The main script is `main.py`. Youc an check all the available 

## Training the model
- `python main.py --experiment_name=baseline --mode=train` should start training the baseline model.
## Evaluating the model
- `python main.py --train_dir=baseline --mode=eval` will evaluate the model (give F1 and EM scores) trained in the experiment named `baseline`.
## Inspecting output
- `python main.py --train_dir=baseline --mode=show_examples` will output 10 randomly selected samples of (context, question, predicted answer, true answer) for `baseline` model.

### Attention model config
There are couple of switches to configure thee attention mechanism for the model.
- `--attention_model` takes two values `uni-dir` (default) and `bi-dir`.
- `--attention_weight` takes two values `weighted` and `unweighted` (default).
### Adversarial training config
- `--eval_squad_2` flag sets the model to train on SQuAD 2.0 datatset.
- `--na_bias` takes two values `b`(default) and `w` for simple-bias and aggregated-bias as described in the paper.

# Acknowledgement
Big shout out to authors of [cs224n-win18-squad]! This code is based off of it.

----
----

# APPENDIX

Reading comprehension task can expose the model's understanding of the language and [meaning](https://plato.stanford.edu/entries/meaning/). Below are some of the datasets and possible ways of how they fall short on evaluating the model's true understanding of language and meaning.

## Datasets
- [Squad 1.1][1]
  * SOTA models trained on this dataset miserably fail in the face of [adverserial examples].
  * Simple [heuristic based model] performs near SOTA, putting the increasing complex models in perspective.
  * Has all answerable questions (forces the model to answer a question when no correct answer exists).
  * Perturb the dataset by associating the [questions with other paragraphs] to artificially generate unanswerable questions to make the model more robust.
  
  **Possible experiment**: 
  * Shuffle the sentences of each paragraph and study the behaviour of the models. Shuffling the sentences in the paragraph might change the answers or in most cases make the answer ambiguous.
- [Squad 2.0][2] (with unanswerable questions)
  * Makes the dataset harder by including questions with high token overlap with the context paragraph and also with plausible answer (same POS type) but no correct answer from the passage. This reinforces the model to have a greater understanding of language than pattern matching.
  
  **Possible experiment**: 
  * Evaluate current SOTA models on Squad 2.0. Find the % of negetive examples that the model correctly deemed unanswerable. Add answers to those correclty predicted negative examples and check if the model answers now. (Still need to concretely formulate how to add answers to previously unanswerable questions.)

## Hypothesis tested in this code base:
* A variant of BiDAF model was trained on both Squad 1.1 and Squad 2.0. Both models were compared against their performance on adversarial test set released by [Robin et. al]. If the model trained on Squad 2.0 performs better, this prooves the hypothesis that Squad 2.0 improves the language understanding capabilities of the models.
 
 [1]: https://arxiv.org/abs/1606.05250
 [2]: https://arxiv.org/abs/1806.03822
 [adverserial examples]: https://arxiv.org/abs/1707.07328
 [Robin et. al]: https://arxiv.org/abs/1707.07328
 [heuristic based model]: https://arxiv.org/abs/1703.04816
 [questions with other paragraphs]: https://arxiv.org/pdf/1710.10723.pdf
 [cs224n-win18-squad]: https://github.com/abisee/cs224n-win18-squad 
 [Study of Attention Mechanisms and Adversarial Training for Question Answering]: https://drive.google.com/file/d/1Y-cmOsCboaB8R-1QbykbjVM3h-xhywsY/view?usp=sharing

