from manim import *

class Collision2D(Scene):
    def construct(self):
        # Introduction
        title = Text("2D Collisions: Elastic and Inelastic").scale(0.8).to_edge(UP)
        self.play(Write(title))

        intro = Text("In 2D collisions, momentum is conserved in both x and y directions.", font_size=30)
        self.play(FadeIn(intro))
        self.wait(2)
        self.play(FadeOut(intro))

        # Show two masses before collision
        m1 = Circle(radius=0.5, color=BLUE).shift(LEFT * 3)
        m2 = Circle(radius=0.5, color=GREEN).shift(RIGHT * 3)
        label_m1 = Text("m1", font_size=30).next_to(m1, DOWN)
        label_m2 = Text("m2", font_size=30).next_to(m2, DOWN)

        self.play(FadeIn(m1, m2, label_m1, label_m2))

        # Add velocity vectors before collision
        v1 = Arrow(start=m1.get_center(), end=m1.get_center() + RIGHT, buff=0, color=BLUE)
        v2 = Arrow(start=m2.get_center(), end=m2.get_center() + LEFT, buff=0, color=GREEN)
        v1_label = MathTex(r"\mathbf{v_1}").next_to(v1, UP)
        v2_label = MathTex(r"\mathbf{v_2}").next_to(v2, UP)

        self.play(Create(v1), Create(v2), FadeIn(v1_label, v2_label))
        self.wait(2)

        # Momentum conservation equations in x and y directions
        momentum_x_eq = MathTex(r"m_1 v_{1x} + m_2 v_{2x} = m_1 v'_{1x} + m_2 v'_{2x}")
        momentum_y_eq = MathTex(r"m_1 v_{1y} + m_2 v_{2y} = m_1 v'_{1y} + m_2 v'_{2y}")
        momentum_group = VGroup(momentum_x_eq, momentum_y_eq).arrange(DOWN, buff=0.5).to_edge(LEFT)

        self.play(FadeIn(momentum_group))
        self.wait(2)

        # Elastic Collision Example
        elastic_label = Text("Elastic Collision: Momentum and Kinetic Energy Conserved", font_size=25).to_edge(DOWN)
        self.play(FadeIn(elastic_label))

        # Update the scene after the collision (Elastic Case)
        v1_prime = Arrow(start=m1.get_center(), end=m1.get_center() + RIGHT * 0.5 + UP * 0.5, buff=0, color=RED)
        v2_prime = Arrow(start=m2.get_center(), end=m2.get_center() + LEFT * 0.7 + DOWN * 0.2, buff=0, color=RED)
        v1_prime_label = MathTex(r"\mathbf{v'_1}").next_to(v1_prime, UP)
        v2_prime_label = MathTex(r"\mathbf{v'_2}").next_to(v2_prime, UP)

        self.play(Transform(v1, v1_prime), Transform(v2, v2_prime), FadeIn(v1_prime_label, v2_prime_label))
        self.wait(2)

        # Kinetic energy conservation equation
        kinetic_energy_eq = MathTex(r"\frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2 = \frac{1}{2} m_1 v'_1^2 + \frac{1}{2} m_2 v'_2^2").to_edge(LEFT)
        self.play(FadeIn(kinetic_energy_eq))
        self.wait(2)

        # Inelastic Collision
        inelastic_label = Text("Inelastic Collision: Only Momentum is Conserved", font_size=25).to_edge(DOWN)
        self.play(Transform(elastic_label, inelastic_label))

        # Update the scene after the collision (Inelastic Case)
        v_inelastic = Arrow(start=m1.get_center(), end=m1.get_center() + RIGHT * 0.3, buff=0, color=YELLOW)
        v_inelastic_label = MathTex(r"\mathbf{v'}").next_to(v_inelastic, UP)

        self.play(Transform(v1_prime, v_inelastic), Transform(v2_prime, v_inelastic), FadeIn(v_inelastic_label))
        self.wait(2)

        self.play(FadeOut(v1_prime, v2_prime, v1_prime_label, v2_prime_label, momentum_group, kinetic_energy_eq, elastic_label))
        self.wait(2)
