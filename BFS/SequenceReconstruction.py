from typing import (
    List,
)

class SequenceReconstruction:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph, indegree = self.get_indegree(org, seqs)

    def get_indegree(self, org, seqs):
        graph = [[] for i in range(len(org))]
        