class SignalGenerator:
    """Advanced trading signal generation system"""

    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.signals = {}
        self.indicators = {}

    def generate_trading_signals(self, data: pd.DataFrame) -> List[TradingSignal]:
        """Generate trading signals based on multiple indicators"""
        signals = []

        # Calculate indicators
        ma_signals = self._analyze_moving_averages(data)
        rsi_signals = self._analyze_rsi(data)
        macd_signals = self._analyze_macd(data)
        pattern_signals = self._analyze_patterns(data)

        # Combine and filter signals
        combined_signals = self._combine_signals([
            ma_signals,
            rsi_signals,
            macd_signals,
            pattern_signals
        ])

        # Calculate signal strength and generate final signals
        for signal in combined_signals:
            strength = self._calculate_signal_strength(signal, data)
            if strength > self.config.get('min_signal_strength', 0.7):
                entry, stop, target = self._calculate_trade_levels(signal, data)
                signals.append(
                    TradingSignal(
                        symbol=data['symbol'].iloc[-1],
                        timestamp=datetime.now(),
                        signal_type=signal['type'],
                        entry_price=entry,
                        stop_loss=stop,
                        take_profit=target,
                        strength=strength,
                        timeframe=data['timeframe'].iloc[-1],
                        indicators=signal['indicators']
                    )
                )

        return signals

    def _analyze_moving_averages(self, data: pd.DataFrame) -> List[Dict]:
        """Analyze moving average crossovers"""
        signals = []

        # Calculate moving averages
        sma_20 = data['close'].rolling(window=20).mean()
        sma_50 = data['close'].rolling(window=50).mean()

        # Look for crossovers
        if sma_20.iloc[-2] < sma_50.iloc[-2] and sma_20.iloc[-1] > sma_50.iloc[-1]:
            signals.append({
                'type': 'BUY',
                'indicator': 'MA_CROSS',
                'strength': 0.8
            })
        elif sma_20.iloc[-2] > sma_50.iloc[-2] and sma_20.iloc[-1] < sma_50.iloc[-1]:
            signals.append({
                'type': 'SELL',
                'indicator': 'MA_CROSS',
                'strength': 0.8
            })

        return signals