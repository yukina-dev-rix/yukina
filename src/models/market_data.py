@dataclass
class MarketData:
    """Market data structure"""
    symbol: str
    timestamp: datetime
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: float
    indicators: Dict = None