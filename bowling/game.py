from __future__ import annotations
from frames import Frame


class Game:
    def __init__(self: Game) -> None:
        self._frames: list[Frame] = []

    def roll(self: Game, pins: int) -> None:
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be within [0, 10].")

        if self._is_done():
            raise RuntimeError("Game completed.")

        self._get_or_start_frame().roll(pins)

    def _is_done(self: Game) -> bool:
        return len(self._frames) == 10 and self._frames[-1].is_done()

    def _get_or_start_frame(self: Game) -> Frame:
        num_frames: int = len(self._frames)

        if num_frames == 0 or self._frames[-1].is_done():
            self._start_new_frame(num_frames + 1)

        return self._frames[-1]

    def _start_new_frame(self: Game, frame_oridnal: int):
        self._frames.append(Frame.create(frame_oridnal))

    def score(self: Game) -> int:
        score: int = 0

        for i, frame in enumerate(self._frames):
            score += frame.score()
            try:
                if frame.is_spare() or frame.is_strike():
                    score += self._frames[i + 1].rolls[0]

                if frame.is_strike():
                    try:
                        score += self._frames[i + 1].rolls[1]
                    except:
                        score += self._frames[i + 2].rolls[0]
            except IndexError:
                pass

        return score


def main() -> None:
    g1 = Game()
    g1.roll(10)  # frame 1
    g1.roll(10)  # frame 2
    g1.roll(10)  # frame 3
    g1.roll(10)  # frame 4
    g1.roll(10)  # frame 5
    g1.roll(10)  # frame 6
    g1.roll(10)  # frame 7
    g1.roll(10)  # frame 8
    g1.roll(10)  # frame 9
    g1.roll(10)  # frame 10
    g1.roll(10)
    g1.roll(10)
    print(g1.score())

    g2 = Game()
    g2.roll(10)  # frame 1
    g2.roll(9)  # frame 2
    g2.roll(1)
    g2.roll(5)  # frame 3
    g2.roll(5)
    g2.roll(7)  # frame 4
    g2.roll(2)
    g2.roll(10)  # frame 5
    g2.roll(10)  # frame 6
    g2.roll(10)  # frame 7
    g2.roll(9)  # frame 8
    g2.roll(0)
    g2.roll(8)  # frame 9
    g2.roll(2)
    g2.roll(9)  # frame 10
    g2.roll(1)
    g2.roll(10)
    print(g2.score())


if __name__ == "__main__":
    main()
