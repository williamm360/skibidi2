from manim import *
from manim import config as global_config
import numpy as np
from videosManim import VideoMobject

global_config.renderer = "opengl"


class IntroScene(Scene):
    def construct(self):
        # horizontal letters
        name_txt_h = VGroup(*[Tex(c) for c in "SANG-BEV"])
        name_txt_h.arrange(RIGHT).scale(2)

        name_txt_v = VGroup(*[Tex(c) for c in "SANG-BEV"])
        name_txt_v.arrange(DOWN, buff=0.2).scale(1.5).to_edge(
            LEFT
        )  # Added buff for consistent spacing

        full_name_array = [
            Tex(word)
            for word in [
                "Surface",
                "Adaptive",
                "Normal-Oriented",
                "Gaussians",
                "For",
                "Bird's",
                "Eye",
                "View",
            ]
        ]

        descr_txt = (
            Tex("A Solution for monocular zero-shot BEV reconstruction")
            .match_y(name_txt_h)
            .shift(UP * 0.5)
        )
        paper_names = (
            Tex(
                "Presented by Ilian Djorf, Noah Favreau,\\\ Louis Turpault and William Ma"
            )
            .match_y(descr_txt)
            .shift(DOWN * 1.5)
        )
        credit_txt = Tex("Animated with ManimCE").match_y(paper_names).shift(DOWN * 1.5)

        for word in full_name_array:
            word.scale(1.5)
        extra_buff = 0.3
        name_txt_v[4].shift(DOWN * extra_buff)
        for i in range(5, len(name_txt_v)):
            name_txt_v[i].shift(DOWN * extra_buff * 2)

        method_outline = Rectangle(
            width=6,
            height=3.5,
            color=WHITE,
            stroke_width=4,
        )

        method_outline.set_style(stroke_width=4, stroke_opacity=0.8)
        method_outline = DashedVMobject(method_outline, num_dashes=60)
        method_outline.to_corner(UL).shift(DOWN * 0.35).shift(LEFT * 0.25)

        application_outline = Rectangle(
            width=6,
            height=2.5,
            color=WHITE,
            stroke_width=4,
        )

        application_outline.set_style(stroke_width=4, stroke_opacity=0.8)
        application_outline = DashedVMobject(application_outline, num_dashes=60)
        application_outline.to_corner(DL).shift(DOWN * 0.25).shift(LEFT * 0.25)

        method_txt = Tex("Method").next_to(method_outline, RIGHT * 1.2)
        application_txt = Tex("Application").next_to(application_outline, RIGHT * 1.2)

        self.play(Create(name_txt_h, run_time=0.7))
        self.wait(0.7)

        self.play(name_txt_h.animate.shift(UP * 2), run_time=1)
        self.wait(0.6)
        self.play(Create(descr_txt))
        self.wait(0.6)
        self.play(Create(paper_names))
        self.wait(0.6)
        self.play(Create(credit_txt))
        self.wait(1.5)
        self.play(
            FadeOut(descr_txt), FadeOut(paper_names), FadeOut(credit_txt), run_time=1
        )
        self.wait(0.8)
        self.play(ReplacementTransform(name_txt_h, name_txt_v), run_time=1.5)

        self.wait(0.5)
        desc_comp = VGroup(
            Text("SANG-BEV is a upgrade from existing"),
            Text("Bird Eye view techniques by using"),
            Text("state-of-the-art normal map models"),
            Text("found previously in depth maps "),
            Text("model regression "),
        ).arrange(DOWN)

        self.play(Write(desc_comp))
        self.wait(3)
        self.play(FadeOut(desc_comp))
        self.wait(0.5)

        # vertical letters -> full words
        for v_letter, word in zip(name_txt_v, full_name_array):
            # Position word to match the letter's vertical center, left-align to screen edge
            word.match_y(v_letter)  # Match vertical position
            word.to_edge(LEFT)  # Align all words to left edge consistently

            # remove letter and show word
            self.play(FadeOut(v_letter), FadeIn(word), run_time=0.4)

        self.wait(1)
        self.play(
            full_name_array[0].animate.set_color(BLUE).shift(RIGHT),
            full_name_array[1].animate.set_color(BLUE).shift(RIGHT),
            run_time=1,
        )
        SurfaceAdaptiveHint.subscene_animation(self)
        self.wait(1)
        self.play(
            full_name_array[0].animate.set_color(BLUE_A).shift(LEFT),
            full_name_array[1].animate.set_color(BLUE_A).shift(LEFT),
            full_name_array[2].animate.set_color(GREEN).shift(RIGHT),
            run_time=1,
        )

        video_normal = (
            VideoMobject(r"media/videos/main/1080p15/NormalOrientedHint.mp4")
            .scale(0.9)
            .to_edge(RIGHT)
        )
        video_normal.set_z_index(-1)
        self.add(video_normal)
        self.wait(video_normal.duration)
        self.play(FadeOut(video_normal))

        self.wait(1)
        self.play(
            full_name_array[2].animate.set_color(GREEN_A).shift(LEFT),
            full_name_array[3].animate.set_color(RED).shift(RIGHT),
            run_time=1,
        )
        video_gaussian = (
            VideoMobject(r"media/videos/main/1080p15/SmoothGaussianTransition.mp4")
            .scale(0.9)
            .to_edge(RIGHT)
        )
        self.add(video_gaussian)
        self.wait(video_gaussian.duration)
        self.play(FadeOut(video_gaussian))
        self.wait(1)
        self.play(
            full_name_array[3].animate.set_color(RED_A).shift(LEFT),
            full_name_array[5].animate.set_color(YELLOW).shift(RIGHT),
            full_name_array[6].animate.set_color(YELLOW).shift(RIGHT),
            full_name_array[7].animate.set_color(YELLOW).shift(RIGHT),
            run_time=1,
        )
        BEVHint.create_scene(self)
        self.wait(1)
        self.play(
            full_name_array[5].animate.set_color(YELLOW_A).shift(LEFT),
            full_name_array[6].animate.set_color(YELLOW_A).shift(LEFT),
            full_name_array[7].animate.set_color(YELLOW_A).shift(LEFT),
            run_time=1,
        )
        self.wait(1)
        self.play(Create(method_outline))
        self.wait(0.5)
        self.play(Create(method_txt), run_time=0.5)
        self.wait()
        self.play(Create(application_outline))
        self.wait(0.5)
        self.play(Create(application_txt), run_time=0.5)
        self.wait(2)

        self.play(
            FadeOut(method_outline),
            FadeOut(method_txt),
            FadeOut(application_outline),
            FadeOut(application_txt),
        )

        self.play(*[mob.animate.shift(LEFT * 20) for mob in self.mobjects])
        self.wait(1)
        end = VGroup(
            Text("Thanks for watching"),
            Text("For more information"),
            Text("Visit the Powerpoint!"),
        ).arrange(DOWN)

        self.play(Write(end))
        self.wait(2)


class SurfaceAdaptiveHint:
    @staticmethod
    def subscene_animation(scene):
        wood_texture = ImageMobject("images/main/wood.jpeg").scale(0.08).to_edge(RIGHT)
        snow_texture = (
            ImageMobject("images/main/snow.jpg")
            .scale(0.4256)
            .next_to(wood_texture, UP * 1.3)
        )
        glass_texture = (
            ImageMobject("images/main/glass.jpg")
            .scale(0.133)
            .next_to(wood_texture, DOWN * 1.3)
        )

        frame_wood = SurroundingRectangle(wood_texture, buff=0.2)
        frame_wood.set_stroke(BLUE, 3)
        frame_snow = SurroundingRectangle(snow_texture, buff=0.2)
        frame_snow.set_stroke(BLUE, 3)
        frame_glass = SurroundingRectangle(glass_texture, buff=0.2)
        frame_glass.set_stroke(BLUE, 3)

        scene.play(
            FadeIn(wood_texture),
            Create(frame_wood),
            FadeIn(glass_texture),
            Create(frame_glass),
            FadeIn(snow_texture),
            Create(frame_snow),
        )
        wood_desc = (
            VGroup(
                Text("Grain Lines", font_size=20),
                Text("Strong Edges", font_size=20),
                Text("Matte Surface", font_size=20),
            )
            .arrange(DOWN)
            .match_y(frame_wood)
            .set_x(1)
        )
        snow_desc = (
            VGroup(
                Text("High Albedo", font_size=20),
                Text("Grainy Texture", font_size=20),
                Text("Irregular Coverage", font_size=20),
            )
            .arrange(DOWN)
            .match_y(frame_snow)
            .set_x(1)
        )
        glass_desc = (
            VGroup(
                Text("High Transparency", font_size=20),
                Text("Sharp Reflections", font_size=20),
                Text("Strong Highlights", font_size=20),
            )
            .arrange(DOWN)
            .match_y(frame_glass)
            .set_x(1)
        )

        scene.wait(2)
        scene.play(Write(snow_desc))
        scene.wait(2)
        scene.play(Write(wood_desc))
        scene.wait(2)
        scene.play(Write(glass_desc))
        scene.wait(3)

        scene.play(
            FadeOut(wood_texture),
            FadeOut(frame_wood),
            FadeOut(glass_texture),
            FadeOut(frame_glass),
            FadeOut(snow_texture),
            FadeOut(frame_snow),
            FadeOut(wood_desc),
            FadeOut(snow_desc),
            FadeOut(glass_desc),
        )


class NormalOrientedHint(ThreeDScene):
    def construct(self):
        # Start with a view that shows the tilted line clearly
        self.set_camera_orientation(
            phi=90 * DEGREES,  # Slight tilt up from horizontal
            theta=-90 * DEGREES,  # Side view
        )

        # 3D axes
        axes = ThreeDAxes(
            x_range=[-0.5, 4],
            y_range=[-0.5, 4],
            z_range=[-0.5, 4],
        )

        self.add(axes)

        # Line ON the plane z=x
        line_2d = Line(
            start=axes.c2p(0, 0, 0), end=axes.c2p(2, 0, 2), color=BLUE, stroke_width=6
        )

        # Normal perpendicular to plane z=x
        normal_vec = np.array([-1, 0, 1]) / np.sqrt(2)

        normal_2d = Arrow3D(
            start=axes.c2p(1, 0, 1), end=axes.c2p(1, 0, 1) + normal_vec * 1.5, color=RED
        )

        # Show line and normal
        self.play(Create(line_2d))
        self.play(GrowFromPoint(normal_2d, point=normal_2d.get_start()))
        self.wait(1)

        # TRIANGLE surface (not square!) on plane z=x
        # Vertices: (0,0,0), (2,0,2), (0,2,0)
        tri_3d = Surface(
            lambda u, v: axes.c2p(
                u,
                v * (2 - u),  # This creates triangular region
                u,
            ),
            u_range=[0, 2],
            v_range=[0, 1],  # v from 0 to 1, scaled by (2-u)
            resolution=(4, 4),
            fill_opacity=0.6,
            fill_color=BLUE,
        )

        # Triangle boundary
        boundary = Polygon(
            axes.c2p(0, 0, 0),
            axes.c2p(2, 0, 2),
            axes.c2p(0, 2, 0),
            color=WHITE,
            stroke_width=3,
        )

        # Normal at triangle center
        center = axes.c2p(2 / 3, 2 / 3, 2 / 3)
        self.normal_3d = Arrow3D(start=center, end=center + normal_vec * 1.5, color=RED)
        scene_group = VGroup(axes, tri_3d, boundary, self.normal_3d, normal_2d)

        self.move_camera(
            phi=60 * DEGREES,
            added_anims=[
                FadeOut(line_2d),
                FadeIn(tri_3d),
                FadeIn(boundary),
                Transform(normal_2d, self.normal_3d),
            ],
        )
        # Expand line to triangle
        self.move_camera(
            # phi=60 * DEGREES,
            theta=-230 * DEGREES,
            added_anims=[scene_group.animate.shift(UP * 3 + RIGHT * 2)],
            run_time=2,
        )
        formula = MathTex(
            r"\cos \theta = \frac{\vec a \cdot \vec b}{\lVert \vec a \rVert \, \lVert \vec b \rVert}"
        ).to_corner(UR)

        # Manually color by finding the tex strings
        formula.set_color_by_tex(r"\vec a", RED)
        formula.set_color_by_tex(r"\vec b", ORANGE)

        ghost_plane = tri_3d.copy()

        self.ghost_normal = self.normal_3d.copy()

        # Rotate around multiple axes for more disturbance

        ghost_plane.set_fill(GREEN, opacity=0.3)
        self.ghost_normal.set_color(ORANGE)

        # Show ghost plane
        self.play(FadeIn(ghost_plane), FadeIn(self.ghost_normal))
        self.wait(1)

        # Display angle

        # Create text that updates in real-time
        angle_text = always_redraw(
            lambda: (
                VGroup(
                    MathTex(f"\\theta = {self.get_angle_between_normals():.1f}^\\circ"),
                    MathTex(
                        f"\\cos(\\theta) = {np.cos(self.get_angle_between_normals() * DEGREES):.3f}"
                    ),
                )
                .arrange(DOWN)
                .to_corner(UL)
                .add_background_rectangle()
            )
        )

        # Add text with updater
        self.add_fixed_in_frame_mobjects(angle_text)

        # Then animate it appearing
        self.play(FadeIn(angle_text))
        self.add_fixed_in_frame_mobjects(formula)
        self.play(
            Rotate(ghost_plane, 5 * DEGREES, axis=UP),
            Rotate(ghost_plane, 10 * DEGREES, axis=RIGHT),
            Rotate(self.ghost_normal, 5 * DEGREES, axis=UP),
            Rotate(self.ghost_normal, 10 * DEGREES, axis=RIGHT),
            FadeIn(formula),
        )
        self.play(
            Rotate(ghost_plane, -10 * DEGREES, axis=UP),
            Rotate(self.ghost_normal, -10 * DEGREES, axis=UP),
            run_time=2,
        )
        self.play(
            Rotate(ghost_plane, 20 * DEGREES, axis=UP),
            Rotate(self.ghost_normal, 20 * DEGREES, axis=UP),
            run_time=2,
        )
        self.play(
            Rotate(ghost_plane, -5 * DEGREES, axis=UP),
            Rotate(self.ghost_normal, -5 * DEGREES, axis=UP),
            run_time=2,
        )
        self.play(
            Rotate(ghost_plane, -10 * DEGREES, axis=UP),
            Rotate(self.ghost_normal, -10 * DEGREES, axis=UP),
            run_time=2,
        )
        self.play(
            Rotate(ghost_plane, 10 * DEGREES, axis=RIGHT),
            Rotate(self.ghost_normal, 10 * DEGREES, axis=RIGHT),
            run_time=1,
        )
        self.play(
            Rotate(ghost_plane, -30 * DEGREES, axis=RIGHT),
            Rotate(self.ghost_normal, -30 * DEGREES, axis=RIGHT),
            run_time=2,
        )
        self.play(
            Rotate(ghost_plane, 10 * DEGREES, axis=RIGHT),
            Rotate(self.ghost_normal, 10 * DEGREES, axis=RIGHT),
            run_time=1,
        )
        self.wait()

    def get_angle_between_normals(self):
        # Extract current normal directions
        original_dir = self.normal_3d.get_end() - self.normal_3d.get_start()
        ghost_dir = self.ghost_normal.get_end() - self.ghost_normal.get_start()

        original_dir = original_dir / np.linalg.norm(original_dir)
        ghost_dir = ghost_dir / np.linalg.norm(ghost_dir)

        cos_angle = np.dot(original_dir, ghost_dir)
        angle_deg = np.arccos(np.clip(cos_angle, -1, 1)) * 180 / np.pi
        return angle_deg


class GaussiansHint(ThreeDScene):
    def construct(self):
        # Start with a good angle to see the floor plane
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        # Axes: x,z on floor (horizontal), y points UP (probability)
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[0, 0.5, 0.1],  # Y is HEIGHT (probability)
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=3,
            z_length=6,
        )
        self.add(axes)
        axes.z_axis.set_opacity(0)

        # ============ 1D GAUSSIAN ============
        title1 = Text("1D Gaussian", font_size=40).to_corner(UL)
        self.add_fixed_in_frame_mobjects(title1)
        self.play(FadeIn(title1))

        # 1D curve in x-y plane (z=0), probability is HEIGHT
        def gaussian_1d(x):
            return 0.4 * np.exp(-(x**2) / 2)

        curve = ParametricFunction(
            lambda t: axes.c2p(t, gaussian_1d(t), 0),  # (x, prob, z=0)
            t_range=[-3, 3],
            color=BLUE,
            stroke_width=5,
        )

        self.play(Create(curve), run_time=2)
        self.wait(2)

        # ============ 2D GAUSSIAN ============
        title2 = Text("2D Gaussian", font_size=40).to_corner(UL)
        self.add_fixed_in_frame_mobjects(title2)

        # Surface: x,z on floor, y (height) is probability
        def gaussian_2d(u, v):
            return 0.4 * np.exp(-(u**2 + v**2) / 2)

        surface = Surface(
            lambda u, v: axes.c2p(u, gaussian_2d(u, v), v),  # (x, prob, z)
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(10, 10),
            fill_opacity=0.8,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )

        # Smooth transition
        self.move_camera(
            phi=-20 * DEGREES,
            added_anims=[
                FadeOut(title1),
                FadeIn(title2),
                ReplacementTransform(curve, surface),
                axes.z_axis.animate.set_opacity(1),
            ],
            run_time=2.5,
        )
        self.wait(1)

        # START ROTATION HERE (after 2D appears)
        self.begin_ambient_camera_rotation(rate=0.12, about="phi")
        self.wait(6)  # Rotate for a bit while showing 2D

        # ============ 3D GAUSSIAN TRANSITION ============
        title3 = (
            VGroup(Text("3D Gaussian", font_size=36), Text("(spherical)", font_size=24))
            .arrange(DOWN, aligned_edge=LEFT)
            .to_corner(UL)
        )
        self.add_fixed_in_frame_mobjects(title3)

        # NEW centered axes for 3D
        axes_3d = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            z_length=6,
        )

        # Create SPHERICAL Gaussian first (isotropic)
        n_shells = 10
        gaussian_spherical = VGroup()
        max_radius = 2.8

        for i in range(n_shells):
            r = (i + 1) / n_shells * max_radius
            sigma = 1.0
            prob = np.exp(-(r**2) / (2 * sigma**2))

            sphere = Sphere(radius=r, resolution=(18, 18))

            # Color gradient
            if prob > 0.6:
                color = interpolate_color(RED, YELLOW, (1 - prob) / 0.4)
            else:
                color = interpolate_color(YELLOW, BLUE, (0.6 - prob) / 0.6)

            sphere.set_fill(color, opacity=0.18)
            sphere.set_stroke(color, width=1, opacity=0.4)

            gaussian_spherical.add(sphere)

        # Transition to 3D spherical
        self.play(
            FadeOut(title2),
            FadeIn(title3),
            FadeOut(axes),
            FadeIn(axes_3d),
            FadeOut(surface),
            FadeIn(gaussian_spherical),
            run_time=2.5,
        )
        self.wait(1)

        # Add legend
        legend = (
            VGroup(
                Text("High P", color=RED, font_size=28),
                Text("Mid P", color=YELLOW, font_size=28),
                Text("Low P", color=BLUE, font_size=28),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_corner(DR)
        )
        self.add_fixed_in_frame_mobjects(legend)
        self.play(FadeIn(legend))

        self.wait(2)

        # ============ TRANSITION TO ORIENTED GAUSSIAN ============
        title4 = (
            VGroup(
                Text("3D Gaussian", font_size=36),
                Text("(with covariance)", font_size=24),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_corner(UL)
        )
        self.add_fixed_in_frame_mobjects(title4)

        # Define covariance matrix - elongated diagonally
        cov_matrix = np.array([[2.0, 0.6, 0.3], [0.6, 2.0, 0.3], [0.3, 0.3, 0.5]])

        # Eigendecomposition
        eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

        # Find the direction of maximum variance (main direction)
        max_variance_idx = np.argmax(eigenvalues)
        primary_direction = eigenvectors[:, max_variance_idx]

        print(f"Gaussian points towards: {primary_direction}")
        print(f"With variance (eigenvalue): {eigenvalues[max_variance_idx]}")

        # Create ORIENTED Gaussian
        gaussian_oriented = VGroup()

        for i in range(n_shells):
            num_std_devs = (i + 1) / n_shells * 2.5

            # Create ellipsoid
            sphere = Sphere(radius=1, resolution=(18, 18))

            # Scale by eigenvalues
            for axis, eigenval in enumerate(eigenvalues):
                std_dev = np.sqrt(np.abs(eigenval))
                sphere.stretch(std_dev * num_std_devs, axis)

            # Rotate by eigenvectors
            sphere.apply_matrix(eigenvectors)

            # Probability
            prob = np.exp(-(num_std_devs**2) / 2)

            # Color
            if prob > 0.6:
                color = interpolate_color(RED, YELLOW, (1 - prob) / 0.4)
            else:
                color = interpolate_color(YELLOW, BLUE, (0.6 - prob) / 0.6)

            sphere.set_fill(color, opacity=0.18)
            sphere.set_stroke(color, width=1, opacity=0.4)

            gaussian_oriented.add(sphere)

        # FIRST: Transform spherical to oriented
        self.play(
            FadeOut(title3),
            FadeIn(title4),
            Transform(gaussian_spherical, gaussian_oriented),
            run_time=3,
        )
        self.wait(1)

        # THEN: Show the primary direction arrow
        primary_arrow = Arrow3D(
            start=ORIGIN
            - primary_direction * np.sqrt(eigenvalues[max_variance_idx]) * 4,
            end=primary_direction * np.sqrt(eigenvalues[max_variance_idx]) * 4,
            color=RED,
            thickness=0.04,
        )

        self.play(FadeIn(primary_arrow))

        # Add label

        self.wait(10)

        self.stop_ambient_camera_rotation()


class BEVHint:
    @staticmethod
    def create_scene(scene):
        map_view = Rectangle(height=3.3, width=4.4).to_edge(UR)
        true_view = Rectangle(height=3.3, width=4.4).to_edge(DR)
        map_txt = (
            Text("BEV View", font_size=32).rotate(90 * DEGREES).next_to(map_view, LEFT)
        )
        image_txt = (
            Text("Image", font_size=32).rotate(90 * DEGREES).next_to(true_view, LEFT)
        )

        image_cabin = ImageMobject("images/main/cabin.jpg")
        image_cabin.stretch_to_fit_height(true_view.height)
        image_cabin.stretch_to_fit_width(true_view.width)
        image_cabin.move_to(true_view)

        scene.play(Create(map_view))
        scene.play(Create(true_view))
        scene.play(Create(map_txt))
        scene.play(Create(image_txt))
        scene.play(
            FadeIn(image_cabin), map_view.animate.set_fill(color=GRAY_A, opacity=0.6)
        )

        tree_rect_img = (
            Rectangle(height=3, width=0.4, color=RED)
            .set_z_index(4)
            .next_to(image_cabin, RIGHT)
            .shift(LEFT * 0.8 + UP * 0.1)
            .set_fill(color=RED, opacity=0.6)
        )
        house_rect_img = (
            Rectangle(height=1.3, width=1.6, color=BLUE)
            .set_z_index(2)
            .next_to(tree_rect_img, LEFT)
            .shift(LEFT * 0.18 + UP * 0.5)
            .set_fill(color=BLUE, opacity=0.6)
        )
        path_rect_img = (
            Rectangle(height=1.5, width=1.8, color=YELLOW)
            .set_z_index(3)
            .next_to(tree_rect_img, LEFT)
            .shift(LEFT * 0.2 + DOWN * 0.9)
            .set_fill(color=YELLOW, opacity=0.6)
        )
        forest_rect_img = (
            Rectangle(height=1.5, width=1.6, color=PINK)
            .set_z_index(1)
            .next_to(image_cabin, RIGHT)
            .shift(LEFT * 1.9 + UP * 0.8)
            .set_fill(color=PINK, opacity=0.6)
        )
        bush_rect_img = (
            Rectangle(height=1.5, width=0.3, color=ORANGE)
            .set_z_index(1)
            .next_to(house_rect_img, LEFT)
            .shift(LEFT * 0.2 + UP * 0.25)
            .set_fill(color=ORANGE, opacity=0.6)
        )

        forest_rect_bev = (
            Rectangle(width=1.8, height=0.6, color=PINK)
            .to_corner(UR)
            .set_fill(color=PINK, opacity=0.6)
        )
        tree_circle_bev = (
            Circle(radius=0.1, color=RED)
            .next_to(forest_rect_bev, DOWN)
            .shift(DOWN * 2)
            .set_fill(color=RED, opacity=0.6)
        )
        house_rect_bev = (
            Rectangle(width=1.8, height=1.4, color=BLUE)
            .rotate(-30 * DEGREES)
            .next_to(forest_rect_bev, DOWN)
            .shift(LEFT * 1 + UP * 0.7)
            .set_fill(color=BLUE, opacity=0.6)
            .set_z_index(10)
        )
        path_rect_bev = (
            Rectangle(width=1.2, height=1.6, color=YELLOW)
            .rotate(20 * DEGREES)
            .next_to(tree_circle_bev, LEFT)
            .shift(UP * 0.5 + LEFT * 0.2)
            .set_fill(color=YELLOW, opacity=0.6)
        )
        bush_circle_bev = (
            Circle(radius=0.1, color=ORANGE)
            .next_to(house_rect_bev, LEFT)
            .shift(LEFT * 0.3 + UP * 0.2)
            .set_fill(color=ORANGE, opacity=0.6)
        )
        clipped_image = Intersection(path_rect_bev, map_view, color=YELLOW).set_fill(
            color=YELLOW, opacity=0.6
        )

        scene.play(Create(tree_rect_img), Create(tree_circle_bev))

        scene.play(Create(house_rect_img), Create(house_rect_bev))

        scene.play(Create(path_rect_img), Create(clipped_image))

        scene.play(Create(forest_rect_img), Create(forest_rect_bev))

        scene.play(Create(bush_rect_img), Create(bush_circle_bev))
        scene.wait(2)

        scene.play(
            FadeOut(tree_circle_bev),
            FadeOut(tree_rect_img),
            FadeOut(house_rect_bev),
            FadeOut(house_rect_img),
            FadeOut(forest_rect_bev),
            FadeOut(forest_rect_img),
            FadeOut(bush_circle_bev),
            FadeOut(bush_rect_img),
            FadeOut(clipped_image),
            FadeOut(path_rect_img),
            FadeOut(map_view),
            FadeOut(true_view),
            FadeOut(map_txt),
            FadeOut(image_txt),
            FadeOut(image_cabin),
        )
