from collections import Counter, deque

class AIEngine:
    def __init__(self):
        self.history = deque(maxlen=500)  # digits (0–9)

    def add_result(self, digit):
        self.history.append(int(digit))

    def _weighted_scores(self):
        hist = list(self.history)
        score = {}

        for i, num in enumerate(hist[::-1]):
            if i < 10:
                w = 3   # page 1 (trend)
            elif i < 20:
                w = 2   # page 2 (trend+pattern)
            else:
                w = 1   # page 50 (deep)

            score[num] = score.get(num, 0) + w

        return score

    def predict(self):
        if len(self.history) < 15:
            return "COLLECTING", 0, [], []

        score = self._weighted_scores()

        small = {k:v for k,v in score.items() if k <= 4}
        big   = {k:v for k,v in score.items() if k >= 5}

        top_small = sorted(small.items(), key=lambda x: x[1], reverse=True)[:2]
        top_big   = sorted(big.items(), key=lambda x: x[1], reverse=True)[:2]

        sum_small = sum(small.values())
        sum_big   = sum(big.values())

        pred = "BIG" if sum_big > sum_small else "SMALL"
        total = sum_big + sum_small
        conf = int((max(sum_big, sum_small) / total) * 100) if total else 50

        return pred, conf, top_small, top_big
