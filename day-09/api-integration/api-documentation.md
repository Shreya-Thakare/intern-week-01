# API Integration Notes (Day 9)

The Angular dashboard expects a REST API compatible with the Day 8 Laravel routes.

## Base URL
`http://localhost:8000/api`

## Endpoints used

### GET /facilities
Returns facility list used for metrics, search, filter and sort.

### GET /facilities/{id}/inspections
Returns inspection history for the selected facility.

### POST /inspections
Body:
```json
{
  "facility_id": 1,
  "inspection_date": "2026-09-25",
  "cleanliness_score": 6.5,
  "odor_score": 4,
  "waste_level": 3,
  "status": "Good",
  "remarks": "Optional"
}
```

## Offline behaviour
`FacilityService` falls back to in-memory sample data if the API is unreachable so the UI remains demonstrable.
