from __future__ import annotations


class Frame:
    @staticmethod
    def create(oridnal: int) -> (Frame | Frame10):
        if oridnal < 1 or oridnal > 10:
            raise ValueError("Frame ordinal must be within [1, 10].")

        if oridnal == 10:
            return Frame10()

        return Frame()

    def __init__(self: Frame) -> None:
        self.rolls: list[int] = []

    def roll(self: Frame, pins: int) -> None:
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be within [0, 10].")

        if self.is_done():
            raise RuntimeError("Frame completed.")

        self.rolls.append(pins)

    def is_done(self: Frame) -> bool:
        return self.is_strike() or len(self.rolls) == 2

    def is_strike(self: Frame) -> bool:
        return len(self.rolls) == 1 and self.rolls[0] == 10

    def is_spare(self: Frame) -> bool:
        return len(self.rolls) == 2 and sum(self.rolls) == 10

    def score(self: Frame) -> int:
        return sum(self.rolls)


class Frame10(Frame):
    def is_done(self: Frame10) -> bool:
        return len(self.rolls) == 3 or (len(self.rolls) == 2 and self.score() < 10)

    def is_strike(self: Frame10) -> bool:
        return len(self.rolls) >= 1 and self.rolls[0] == 10

    def is_spare(self: Frame10) -> bool:
        return len(self.rolls) >= 2 and self.rolls[0] < 10 and sum(self.rolls[:2]) == 10
