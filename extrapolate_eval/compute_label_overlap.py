###
# This script computes the passage overlap between two qrel files.
###
import argparse
from tqdm import tqdm
from typing import Set, List, Dict
from collections import defaultdict


def load_qrels(qrel_path: str, rel_threshold: int):
    query2pids, all_postive_pids = defaultdict(list), set()
    for line in tqdm(open(qrel_path)):
        qid, _, pid, rel = line.split()
        if int(rel) >= rel_threshold:
            query2pids[qid].append(pid)
            all_postive_pids.add(pid)
        else:
            # so all qids are in the keys
            query2pids[qid] 
    return dict(query2pids), all_postive_pids


def compute_overlap(train_pos_pids: Set[str], test_qrels: Dict[str, Set[str]]):
    overlap_cnt = 0
    for test_pos_pids in test_qrels.values():
        overlap = set(test_pos_pids) & train_pos_pids
        overlap_cnt += 1 if len(overlap) > 1 else 0
    return overlap_cnt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_qrel_path", type=str, required=True, 
        help="TREC-Style qrel file for training.")
    parser.add_argument("--train_rel_threshold", type=int, default=1,
        help="Convert multi-scale relevance labels to binary. If the relevance label is larger or equal to the threshold, the passages are regarded as positive, otherwise negative.")
    parser.add_argument("--test_qrel_path", type=str, required=True,
        help="TREC-Style qrel file for training.")
    parser.add_argument("--test_rel_threshold", type=int, default=1,
        help="Convert multi-scale relevance labels to binary. If the relevance label is larger or equal to the threshold, the passages are regarded as positive, otherwise negative.")
    args = parser.parse_args()

    _, train_pos_pids = load_qrels(args.train_qrel_path, args.train_rel_threshold)
    print(f"Training data has {len(train_pos_pids)} passages.")
    
    test_qrels, _ = load_qrels(args.test_qrel_path, args.test_rel_threshold)

    overlap_cnt = compute_overlap(train_pos_pids, test_qrels)
    overlap_percentage = overlap_cnt / len(test_qrels) * 100
    print(f"Among {len(test_qrels)} test queries, {overlap_cnt} ({overlap_percentage:.1f}%) queries are passage-overlapped. That is, their relelvant passages are also involved in the training data.")
    

if __name__ == "__main__":
    main()