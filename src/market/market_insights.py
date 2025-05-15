class MarketInsights:
    """Advanced market intelligence and insights system"""

    def __init__(self):
        self.sentiment_data = {}
        self.correlations = {}
        self.market_regimes = {}

    async def analyze_market_sentiment(self, symbol: str) -> Dict:
        """Analyze market sentiment from multiple sources"""
        try:
            # Collect data from various sources
            social_sentiment = await self._analyze_social_media_sentiment(symbol)
            news_sentiment = await self._analyze_news_sentiment(symbol)
            technical_sentiment = await self._analyze_technical_sentiment(symbol)

            # Combine sentiment data
            combined_sentiment = self._combine_sentiment_scores([
                social_sentiment,
                news_sentiment,
                technical_sentiment
            ])

            # Generate sentiment report
            sentiment_report = {
                'timestamp': datetime.now(),
                'symbol': symbol,
                'overall_sentiment': combined_sentiment['score'],
                'sentiment_breakdown': {
                    'social': social_sentiment,
                    'news': news_sentiment,
                    'technical': technical_sentiment
                },
                'sentiment_trend': self._calculate_sentiment_trend(symbol),
                'key_factors': combined_sentiment['factors']
            }

            # Update sentiment history
            self._update_sentiment_history(symbol, sentiment_report)

            return sentiment_report

        except Exception as e:
            self.logger.error(f"Error analyzing market sentiment: {e}")
            raise

    async def evaluate_news_impact(self, symbol: str) -> Dict:
        """Evaluate the impact of news on market movement"""
        try:
            # Fetch recent news
            news_data = await self._fetch_news(symbol)

            # Analyze news content
            news_analysis = await self._analyze_news_content(news_data)

            # Calculate price impact
            price_impact = self._calculate_news_price_impact(symbol, news_analysis)

            return {
                'timestamp': datetime.now(),
                'symbol': symbol,
                'news_sentiment': news_analysis['sentiment'],
                'price_impact': price_impact,
                'key_events': news_analysis['key_events'],
                'impact_probability': news_analysis['impact_probability']
            }

        except Exception as e:
            self.logger.error(f"Error evaluating news impact: {e}")
            raise