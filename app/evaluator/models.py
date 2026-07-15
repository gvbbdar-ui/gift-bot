from dataclasses import dataclass

@dataclass
class Gift:
    name: str

    pattern_rarity: float
    model_rarity: float
    background_rarity: float

    supply: int

    floor_price: float

    number_score: float = 0
    liquidity_score: float = 0
