from l42_semantic_model import (
    Problem,
    SemanticStructure,
    semantic_preservation,
    separation_preservation,
    hierarchy_preservation,
    traceability_score,
    classify_mapping,
)

# 元問題 P
P = Problem(
    X=["A", "B", "C", "D", "E", "F"],
    Y={},
    C={},
    T={"goal": "3つの自然複合体を保つこと"},
    R_near_P={("A", "B"), ("C", "D"), ("E", "F")},
    clusters_P=[{"A", "B"}, {"C", "D"}, {"E", "F"}],
)

# S_local: 局所複合体を先に残した写像
S_local = SemanticStructure(
    X=P.X,
    E_plus=[{"A", "B"}, {"C", "D"}, {"E", "F"}],
    E_minus=[{"A", "C"}, {"B", "D"}, {"C", "E"}],
    H=[[{"A", "B"}, {"C", "D"}, {"E", "F"}]],
    psi={
        "E_plus_0": {"source": "cluster_AB"},
        "E_plus_1": {"source": "cluster_CD"},
        "E_plus_2": {"source": "cluster_EF"},
        "E_minus_0": {"source": "separate_AC"},
        "E_minus_1": {"source": "separate_BD"},
        "E_minus_2": {"source": "separate_CE"},
    },
)

# S_flat: 平坦化しすぎた写像
S_flat = SemanticStructure(
    X=P.X,
    E_plus=[{"A", "B", "C"}, {"D", "E", "F"}],
    E_minus=[],
    H=[],
    psi={
        "E_plus_0": {"source": "flat_ABC"},
        "E_plus_1": {"source": "flat_DEF"},
    },
)

for name, S in [("local", S_local), ("flat", S_flat)]:
    m = semantic_preservation(P, S)
    d = separation_preservation(P, S)
    r = traceability_score(S)
    print(f"[{name}]")
    print(f"  M = {m:.3f}")
    print(f"  D = {d:.3f}")
    print(f"  R = {r:.3f}")
    print()

h = hierarchy_preservation(P, S_local, S_flat)
label = classify_mapping(
    m_score=semantic_preservation(P, S_local),
    d_score=separation_preservation(P, S_local),
    h_score=h,
    r_score=traceability_score(S_local),
)

print("[comparison]")
print(f"  H = {h:.3f}")
print(f"  判定 = {label}")
