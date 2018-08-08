from io import StringIO

from farbe import Color, Colored, Farbe


class TestFarbe:

    def setup_method(self, _):
        self.s = 'Hello, 世界😇'
        self.f = Farbe(Color.Fg.Red)
        self.c = self.f.colored(self.s)

    def test_print(self):
        io = StringIO()

        self.f.print(self.s, file=io)

        expected = Color.CSI.format(Color.Fg.Red.value) + self.s + Color.END + '\n'
        assert io.getvalue() == expected

    def test_add_effects(self):
        effects = [Color.Effect.CrossOut, Color.Effect.Italic]
        self.f.add_effects(effects)

        assert set(self.f.effects) == set(effects)

    def test_remove_effects(self):
        f = Farbe(Color.Fg.Red, effects=[Color.Effect.Bold])

        f.remove_effects([Color.Effect.Bold])

        assert set(f.effects) == set()

    def test_colored(self):
        assert type(self.c) == Colored

    def test_colored_plain(self):
        assert self.c.plain() == self.s

    def test_colored_len(self):
        assert len(self.c) == len(self.s)

    def test_colored_add(self):
        s1 = 'hello'
        s2 = 'world'
        red = Farbe(Color.Fg.Red)
        blue = Farbe(Color.Fg.Blue)
        red_text = red.colored(s1)
        blue_text = blue.colored(s2)

        # Colored + Colored
        added = red_text + blue_text
        assert len(red_text) == len(s1)
        assert len(added) == len(s1) + len(s2)
        assert str(added) == str(red_text) + str(blue_text)

        # str + Colored
        added = s1 + blue_text
        assert len(added) == len(s1) + len(blue_text)
        assert str(added) == '\033[0m' + s1 + '\033[0m' + str(blue_text)

        # Colored + str
        added = red_text + s2
        assert len(added) == len(red_text) + len(s2)
        assert str(added) == str(red_text) + '\033[0m' + s2 + '\033[0m'

    def test_colored_build_effect_string(self):
        assert '' == Colored.build_effect_string()

        effects = [Color.Effect.Bold, Color.Effect.Underline]
        effect_string = Colored.build_effect_string(effects)

        expected = '\033[1m\033[4m'
        assert effect_string == expected
