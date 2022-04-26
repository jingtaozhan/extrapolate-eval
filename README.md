# extrapolate-eval

This is the official repo for our paper, [Evaluating Extrapolation Performance of Dense Retrieval](https://arxiv.org/pdf/2204.11447.pdf).
If you are interested in Dense Retrieval and even have conducted experiments on MS MARCO or TREC Deep Learning Tracks, this is the paper/repo you do not want to miss! 

We find surprisingly **high overlap between training data and test data** on the widely-adopted ad hoc retrieval benchmarks. What does it mean for existing benchmark results? How can we resolve such issues?
It means that existing benchmark results are biased toward **interpolation**, i.e., how models perform on queries that are similar to the training queries. Therefore, we propose a simple evaluation protocol to test the **extrapolation performance**, i.e., how models perform on queries that are distinct from the training data. It leads to several non-trivial findings that have been concealed by existing benchmarks. The protocol can also be used in your experiments!

Data and code are coming soon! For now, please enjoy the paper.