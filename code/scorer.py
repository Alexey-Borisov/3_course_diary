from sentence_transformers import CrossEncoder


class CandidateScorer:
    
    def __init__(self, base_model):
        self.base_model = CrossEncoder(base_model)
    
    def score_one(self, query, candidate):
        score = self.base_model.predict([(query, candidate)])
        return score
    
    def score_all(self, query, candidates):
        pairs = [(query, candidate) for candidate in candidates]
        scores = self.base_model.predict(pairs)
        return scores