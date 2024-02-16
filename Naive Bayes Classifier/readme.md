# Naive Bayes Algroithm
## Two conditional Probability are there :
- Independent
  - P(A∩B) = P(A)xp(B)
  - P(A|B) : probabilty of A given B
  - P(A|B) = P(A∩B) / P(B)
- Dependent (Mutually Exclusive)
  - P(A∩B) = 0
  - P(A|B) : probabilty of A given B
  - P(A|B) = P(A∩B) / P(B) = 0
## Now for Naive Bayes derivation we use:
- A and B are two independent event
- P(A|B) = P(A∩B) / P(B)
- P(B|A) = P(B∩A) / P(A)
  - since P(A∩B) = P(B∩A)
- we can say that
- P(A|B) = P(B|A) x P(A) / P(B)
