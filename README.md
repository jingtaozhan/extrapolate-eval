# extrapolate-eval

This is the official repo for our paper, [Evaluating Extrapolation Performance of Dense Retrieval](https://arxiv.org/pdf/2204.11447.pdf).
If you are interested in Dense Retrieval and even have conducted experiments on MS MARCO or TREC Deep Learning Tracks, this is the paper/repo you do not want to miss! 

We find **surprisingly high overlap between training data and test data** on the widely-adopted ad hoc retrieval benchmarks. What does it mean for existing benchmark results? How can we resolve such issues?
It means that existing benchmark results are biased toward **interpolation**, i.e., how models perform on queries that are similar to the training queries. Therefore, we propose a simple evaluation protocol to test the **extrapolation performance**, i.e., how models perform on queries that are distinct from the training data. It leads to several non-trivial findings that have been concealed by existing benchmarks. The evaluation methods can also be used in your experiments!

## Resampled data

TL;DR: We propose to resample the training (and test) data. We remove the overlap to evaluate the extrapolation performance or only keep the overlap to evaluate the interpolation performance. Concretely, we embed the queries based on the query encoder of a Dense Retrieval model and then measure the query similarity based on the cosine-distance of the embeddings. We resample queries based on the query similarity between training and test data. There are two resampling methods.

### Resampling Training Queries (ReSTrain)

ReSTrain samples similar/dissimilar training queries for each test query to construct a new training set for interpolation/extrapolation evaluation. By tuning how many training queries per test query are sampled, we can generate training sets of different sizes. In the paper, we remove the similar training queries of test sets from TREC Deep Learning Tracks in [2019](https://microsoft.github.io/msmarco/TREC-Deep-Learning-2019.html) and [2020](https://microsoft.github.io/msmarco/TREC-Deep-Learning-2020.html). We generate three sizes of training data, i.e., 14k, 45k, and 200k. They are released at [restrain_files/msmarco-passage](./restrain_files/msmarco-passage/). You can simply replace the original MS MARCO training qrels with the new ones and re-train your models. Then the performance on TREC 2019 & 2020 Deep Learning Tracks reflects interpolation/extrapolation capacity.


### Resampling Training and Test Queries (ReSTTest)

ReSTTest clusters training and test queries to K buckets. We train the models with the training queries in K-1 buckets. The test results in those K-1 buckets are interpolation performance and the test results in the remaining one bucket are extrapolation performance. In the paper, K is set to 5. We use ReSTTest to evaluate performance on the large MS MARCO development set (6980 queries). We do not use ReSTrain because if the test set is very large, almost each training query is similar to some test query and thus ReSTrain fails. The resampled training and test data are released at [resttest_files/msmarco-passage](./resttest_files/msmarco-passage/). You can train your models with the training data in the five buckets. The average performance on the interpolation/extrapolation test set corresponds to the final interpolation/extrapolation results.