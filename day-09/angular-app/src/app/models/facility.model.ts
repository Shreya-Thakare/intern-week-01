export interface Facility {
  id: number;
  name: string;
  location: string;
  cleanliness_score: number;
  water_availability: boolean;
}

export interface Inspection {
  id?: number;
  facility_id: number;
  inspection_date: string;
  cleanliness_score: number;
  odor_score: number;
  waste_level: number;
  status: 'Good' | 'Needs Attention' | 'Poor';
  remarks?: string;
}
