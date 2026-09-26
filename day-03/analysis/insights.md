# Key Insights — Facility Hygiene Dataset

1. **Time since last cleaning tracks closely with hygiene risk level.**
   Facilities rated *High* risk had gone 10.06 hours since their last
   cleaning on average, versus only 5.81 hours for *Low* risk facilities —
   nearly double the gap, even though hours-since-cleaning alone is only weakly
   linearly correlated with the raw cleanliness_score, so it behaves more like a
   risk-tier signal than a straight-line predictor.

2. **Water availability strongly affects hygiene outcomes.**
   Facilities with water available were rated *High* risk 22.5% of the time,
   compared to 63.6% for facilities without water access — the single
   clearest categorical split in the dataset.

3. **Hygiene quality varies significantly by location.**
   'Manish Nagar' has the highest average cleanliness score in the dataset,
   while 'Sitabuldi' has the lowest, and 'Sitabuldi' receives
   the most complaints per facility on average — these areas are good candidates
   for prioritized maintenance.

4. **Odor score and complaint volume move together.**
   Odor score and complaints are correlated at 0.59, suggesting
   odor is one of the most noticeable hygiene problems to facility users and a
   useful early-warning feature for prediction models.

5. **Risk class distribution.**
   Of 995 inspected facilities: 313 were
   rated Low risk, 410 Medium risk, and
   272 High risk.
