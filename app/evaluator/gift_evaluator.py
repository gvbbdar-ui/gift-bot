from .models import Gift
from .scoring import rarity_to_score, supply_score

class GiftEvaluator:

    def evaluate(self, gift: Gift):

        pattern = rarity_to_score(
            gift.pattern_rarity
        )

        model = rarity_to_score(
            gift.model_rarity
        )

        background = rarity_to_score(
            gift.background_rarity
        )

        supply = supply_score(
            gift.supply
        )

        gift_score = (
            pattern * 0.40 +
            model * 0.20 +
            background * 0.15 +
            supply * 0.15 +
            gift.number_score * 0.05 +
            gift.liquidity_score * 0.05
        )

        fair_price = self.calculate_price(
            gift_score,
            gift.floor_price
        )

        investment = (
            (fair_price - gift.floor_price)
            /
            gift.floor_price
        ) * 100

        return {
            "gift_score": round(gift_score,2),
            "rarity": round(
                (pattern+model+background)/3,
                2
            ),
            "fair_price": round(
                fair_price,
                2
            ),
            "investment": round(
                investment,
                2
            )
        }

    def calculate_price(
        self,
        score,
        floor
    ):

        return floor * (
            1 + (score / 100) * 0.35
        )
