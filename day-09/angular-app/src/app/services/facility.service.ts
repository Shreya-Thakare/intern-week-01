import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Facility, Inspection } from '../models/facility.model';

@Injectable({ providedIn: 'root' })
export class FacilityService {
  private http = inject(HttpClient);
  private api = 'http://localhost:8000/api';

  /** Offline fallback so the UI works without the Laravel API running */
  private fallbackFacilities: Facility[] = [
    { id: 1, name: 'Central Washroom', location: 'Nagpur Central', cleanliness_score: 5.5, water_availability: true },
    { id: 2, name: 'Cafeteria', location: 'Dharampeth', cleanliness_score: 8.2, water_availability: true },
    { id: 3, name: 'Library Restroom', location: 'Sitabuldi', cleanliness_score: 6.8, water_availability: false },
    { id: 4, name: 'Station Platform WC', location: 'Nagpur Station', cleanliness_score: 4.1, water_availability: true },
  ];

  private fallbackHistory: Record<number, Inspection[]> = {
    1: [
      { id: 1, facility_id: 1, inspection_date: '2026-09-20', cleanliness_score: 5, odor_score: 7, waste_level: 6, status: 'Needs Attention', remarks: 'Cleaning needed' },
    ],
    2: [
      { id: 2, facility_id: 2, inspection_date: '2026-09-20', cleanliness_score: 8, odor_score: 2, waste_level: 2, status: 'Good', remarks: 'Maintained' },
    ],
  };

  list(): Observable<Facility[]> {
    return this.http.get<Facility[]>(`${this.api}/facilities`).pipe(
      catchError(() => of(this.fallbackFacilities))
    );
  }

  history(facilityId: number): Observable<Inspection[]> {
    return this.http
      .get<Inspection[]>(`${this.api}/facilities/${facilityId}/inspections`)
      .pipe(catchError(() => of(this.fallbackHistory[facilityId] || [])));
  }

  addInspection(data: Inspection): Observable<Inspection> {
    return this.http.post<Inspection>(`${this.api}/inspections`, data).pipe(
      catchError(() => {
        const saved = { ...data, id: Date.now() };
        const list = this.fallbackHistory[data.facility_id] || [];
        this.fallbackHistory[data.facility_id] = [saved, ...list];
        return of(saved);
      })
    );
  }
}
