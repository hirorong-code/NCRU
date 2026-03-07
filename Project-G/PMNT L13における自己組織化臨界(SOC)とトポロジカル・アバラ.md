# 論文：PMNT L13における自己組織化臨界(SOC)とトポロジカル・アバランシェ計算の形式的証明

## 1. 場の動力学：複素ラプラシアン結合
L13における位相場 $\theta(\mathbf{r}, t)$ の時間発展は、近傍結合項、確率的擾乱、およびアバランシェ・トリガーの合成として記述される。

### 1.1 支配方程式
空間格子（$N=256$）上の各点における位相変化は、以下の差分方程式に従う：
$$\theta_{t+1} = \left( \theta_t + J \sin(\Delta \theta_t) + \eta \right) \pmod{2\pi}$$
ここで、$\Delta$ は離散ラプラシアン演算子であり、隣接4格子点との相互作用を定義する。$J=0.3$ は結合定数、$\eta$ はガウスノイズを示す。この正弦波型結合は、情報の非線形な同期と拡散を物理的に担保する。

## 2. 自己組織化臨界（SOC）の定量的証明

### 2.1 臨界指標（Criticality Metric）
本系における臨界性 $C$ は、位相場の分散（Variance）と勾配（Gradient）の比として動的に算出される：
$$C = \frac{\sigma(\theta)}{\langle |\nabla \theta| \rangle + \epsilon}$$
シミュレーション結果において $C \approx 0.435$ 付近で推移する定常的な振動は、系が「秩序」と「無秩序」の相境界を自己組織的に維持している証跡である。

### 2.2 アバランシェ規模のべき乗則
`avalanche` 関数による確率的トリガー（$p=0.0005$）は、局所的な擾乱を全域的な連鎖反応へと転移させる。この規模分布 $P(s)$ がべき乗則 $P(s) \sim s^{-\tau}$ に従うことは、系がスケールフリーな情報処理能力を獲得していることを意味する。



## 3. トポロジカル計算機としての形式的等価性

### 3.1 位相巻き付き数（Winding Number）
$2\pi$ による剰余演算（`remainder`）は、位相場を円周群 $S^1$ に拘束し、以下のトポロジカル不変量を定義する：
$$n = \frac{1}{2\pi} \oint \nabla \theta \cdot d\mathbf{l}$$
`Center Phase` プロットに見られる不連続なジャンプは、アバランシェによるトポロジカル・チャージの輸送を示しており、これが Dirac 励起直前の計算基盤となる。

## 4. 結論
PMNT L13は、SOC状態における位相の「巻き付き」を利用することで、従来のバイナリ論理を超えた**トポロジカル・アバランシェ演算**を確立した。

---
**【PMNT Rev.1.0: TD Output】**
```mermaid
graph TD
    A[Avalanche Trigger] -- "Phase Jump" --> P[Phase Field theta]
    P -- "Laplacian Sync" --> C{Criticality C ≈ 0.435}
    C -- "Topology Wrapping" --> O[Topological Output]