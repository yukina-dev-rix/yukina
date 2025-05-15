@dataclass
class TradingSignal:
    """Trading signal structure"""
    symbol: str
    timestamp: datetime
    signal_type: str  # 'BUY' or 'SELL'
    entry_price: float
    stop_loss: float
    take_profit: float
    strength: float
    timeframe: str
    indicators: Dict = None