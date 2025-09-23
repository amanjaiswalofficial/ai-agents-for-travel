from abc import ABC, abstractmethod
import pandas as pd

class BaseRecommender(ABC):
    def __init__(self):
        self.data = None
        self.is_trained = None

    @abstractmethod
    def load_data(self, filepath):
        pass

    @abstractmethod
    def preprocess_data(self):
        pass

    @abstractmethod
    def fit(self):
        """Train/fit the recommender"""
        pass
    
    @abstractmethod
    def recommend(self, n=10, **kwargs):
        """Generate recommendations"""
        pass
    
    def get_stats(self):
        """Get basic statistics about the dataset"""
        if self.data is None:
            return "No data loaded"
        
        return {
            'total_places': len(self.data),
            'avg_rating': self.data['rating'].mean() if 'rating' in self.data.columns else None,
            'columns': list(self.data.columns)
        }
