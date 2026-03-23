from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Set, Tuple

Node = str
Pair = Tuple[Node, Node]
HyperEdge = Set[Node]


def normalize_pair(a: Node, b: Node) -> Pair:
    return tuple(sorted((a, b)))


@dataclass
class Problem:
    """
    P = (X, Y, C, T, R_near_P, clusters_P)
    """
    X: List[Node]
    Y: Dict[str, Any]
    C: Dict[str, Any]
    T: Dict[str, Any]
    R_near_P: Set[Pair]
    clusters_P: List[Set[Node]]


@dataclass
class SemanticStructure:
    """
    S = (X, E_plus, E_minus, H, psi)
    """
    X: List[Node]
    E_plus: List[HyperEdge]
    E_minus: List[HyperEdge]
    H: List[List[Set[Node]]]
    psi: Dict[str, Any]


def pairs_from_hyperedges(edges: Iterable[HyperEdge]) -> Set[Pair]:
    out: Set[Pair] = set()
    for e in edges:
        nodes = list(e)
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                out.add(normalize_pair(nodes[i], nodes[j]))
    return out


def semantic_preservation(problem: Problem, structure: SemanticStructure) -> float:
    """
    M(P,S) = |R_near^P ∩ R_near^S| / |R_near^P|
    """
    if not problem.R_near_P:
        return 1.0
    r_near_s = pairs_from_hyperedges(structure.E_plus)
    return len(problem.R_near_P & r_near_s) / len(problem.R_near_P)


def pair_weight_from_structure(
    structure: SemanticStructure,
    plus_weight: float = 1.0,
    minus_weight: float = 1.0,
    hierarchy_bonus: float = 0.25,
) -> Dict[Pair, float]:
    """
    S から pairwise 重み W_ij を誘導する簡易版。
    """
    weights: Dict[Pair, float] = {}

    for edge in structure.E_plus:
        nodes = list(edge)
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                p = normalize_pair(nodes[i], nodes[j])
                weights[p] = weights.get(p, 0.0) + plus_weight

    for edge in structure.E_minus:
        nodes = list(edge)
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                p = normalize_pair(nodes[i], nodes[j])
                weights[p] = weights.get(p, 0.0) - minus_weight

    for level in structure.H:
        for block in level:
            nodes = list(block)
            for i in range(len(nodes)):
                for j in range(i + 1, len(nodes)):
                    p = normalize_pair(nodes[i], nodes[j])
                    weights[p] = weights.get(p, 0.0) + hierarchy_bonus

    return weights


def avg_intra(cluster: Set[Node], weights: Dict[Pair, float]) -> float:
    nodes = list(cluster)
    vals: List[float] = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            vals.append(weights.get(normalize_pair(nodes[i], nodes[j]), 0.0))
    return sum(vals) / len(vals) if vals else 0.0


def avg_inter(cluster_a: Set[Node], cluster_b: Set[Node], weights: Dict[Pair, float]) -> float:
    vals: List[float] = []
    for a in cluster_a:
        for b in cluster_b:
            vals.append(weights.get(normalize_pair(a, b), 0.0))
    return sum(vals) / len(vals) if vals else 0.0


def separation_preservation(problem: Problem, structure: SemanticStructure) -> float:
    """
    D(P,S) = min intra - max inter
    """
    weights = pair_weight_from_structure(structure)
    if not problem.clusters_P:
        return 0.0

    intra_vals = [avg_intra(cluster, weights) for cluster in problem.clusters_P]
    inter_vals: List[float] = []
    for i in range(len(problem.clusters_P)):
        for j in range(i + 1, len(problem.clusters_P)):
            inter_vals.append(avg_inter(problem.clusters_P[i], problem.clusters_P[j], weights))

    if not intra_vals or not inter_vals:
        return 0.0
    return min(intra_vals) - max(inter_vals)


def hierarchy_preservation(problem: Problem, structure_local: SemanticStructure, structure_flat: SemanticStructure) -> float:
    """
    H(P,S) = D(P,S_local) - D(P,S_flat)
    """
    return separation_preservation(problem, structure_local) - separation_preservation(problem, structure_flat)


def traceability_score(structure: SemanticStructure) -> float:
    """
    R(P,S): 逆参照可能な要素の割合
    """
    total = len(structure.E_plus) + len(structure.E_minus)
    if total == 0:
        return 1.0

    traced = 0
    for i, _ in enumerate(structure.E_plus):
        if f"E_plus_{i}" in structure.psi:
            traced += 1
    for i, _ in enumerate(structure.E_minus):
        if f"E_minus_{i}" in structure.psi:
            traced += 1

    return traced / total


def classify_mapping(
    m_score: float,
    d_score: float,
    h_score: float,
    r_score: float,
    tau_m: float = 0.7,
    tau_d: float = 0.0,
    tau_h: float = 0.0,
    tau_r: float = 0.8,
) -> str:
    """
    L42 前段だけでの簡易判定。
    """
    meaning_ok = m_score >= tau_m and r_score >= tau_r
    separation_ok = d_score >= tau_d
    hierarchy_ok = h_score >= tau_h

    if meaning_ok and separation_ok and hierarchy_ok:
        return "意味保存写像"
    if meaning_ok and not separation_ok:
        return "悪い構造の可能性"
    if not meaning_ok:
        return "悪い写像の可能性"
    return "判定保留"
