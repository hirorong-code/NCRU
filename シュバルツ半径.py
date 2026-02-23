from manim import *
import numpy as np

class BHDeadlock(Scene):
    def construct(self):
        # 1. 初期ポート: NCRU (0-3s)
        ncru_text = Text("NCRU", color=CYAN).scale(2)
        self.play(Write(ncru_text), run_time=1)
        self.wait(2)
        self.play(FadeOut(ncru_text))

        # 2. ブラックホール・コア
        bh_center = Dot(point=ORIGIN, radius=0.5, color=BLACK)
        horizon = Circle(radius=1.5, color=RED, stroke_width=2)
        self.add(bh_center, horizon)

        # 3. データパケット流入 (4-10s)
        particles = VGroup(*[Dot(point=[np.random.uniform(-5, 5), np.random.uniform(-3, 3), 0], 
                                 radius=0.05, color=RED) for _ in range(50)])
        
        def update_particle(p, dt):
            dist = np.linalg.norm(p.get_center())
            if dist > 0.1:
                # シュヴァルツシルトポテンシャルを模した加速
                direction = -p.get_center() / dist
                p.shift(direction * (2 / dist) * dt)
                if dist < 1.5: p.set_color(ORANGE) # 事象の地平線内
        
        particles.add_updater(update_particle)
        self.add(particles)
        self.wait(7) # デッドロック状態の観測
        particles.clear_updaters()

        # 4. 最終ポート: PMNT Conclusion (11-12s)
        # NULL重なりを避けるため、全要素をフェードアウトさせてから結論を表示
        self.play(FadeOut(particles), FadeOut(bh_center), FadeOut(horizon))
        conclusion = Text("PMNT Conclusion", color=WHITE).scale(1.5)
        self.play(FadeIn(conclusion), run_time=1)
        self.wait(1)