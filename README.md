# Reading comprehension
This task can expose the model's understanding of the language and [meaning](https://plato.stanford.edu/entries/meaning/). Below are some of the datasets and possible ways of how they fall short on evaluating the model's true understanding of language and meaning.


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

