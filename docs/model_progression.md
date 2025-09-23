### Level 1: Basic Statistical Models (Start Here)
    1.1 Popularity-Based Recommender
        Simply rank places by rating * number of reviews
        No personalization, same recommendations for everyone
        Features: rating, reviews count
    1.2 Category-Based Filter
        Filter places by main_category or categories
        User says "restaurants" → show top-rated restaurants
        Features: categories, rating
### Level 2: Simple Machine Learning
    2.1 Weighted Scoring Model
        Create composite score using multiple features
        Score = (rating × 0.4) + (review_count_normalized × 0.3) + (other factors × 0.3)
        Features: rating, reviews, is_spending_on_ads, competitors
    2.2 Decision Tree Classifier
        Classify places as "highly recommended" vs "moderately recommended"
        Easy to interpret rules
        Features: rating, reviews, price_range, categories
### Level 3: Content-Based Filtering
    3.1 Simple Text Matching
        Use basic keyword matching on description and categories
        Count common words between user query and place descriptions
    3.2 TF-IDF + Cosine Similarity
        Convert description + categories to TF-IDF vectors
        Find similar places using cosine similarity
        This is where you mentioned wanting to go
    3.3 Advanced NLP
        Use word embeddings (Word2Vec, FastText)
        Semantic similarity rather than just keyword matching
### Level 4: Collaborative Filtering
    4.1 User-Item Matrix (if you get user interaction data)
        Matrix factorization techniques
        Currently you don't have user interaction data
    4.2 Item-Item Collaborative
        "People who liked this place also liked..."
        Based on review_keywords similarity
### Level 5: Hybrid & Advanced Models
    5.1 Hybrid Approach
        Combine content-based + popularity + category filtering
        Weighted ensemble of different models
    5.3 Deep Learning
        Neural networks combining text, numerical, and categorical features
        Embedding layers for categories and locations