import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { FacilityService } from './services/facility.service';
import { Facility, Inspection } from './models/facility.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent implements OnInit {
  private service = inject(FacilityService);
  private fb = inject(FormBuilder);

  facilities: Facility[] = [];
  selected: Facility | null = null;
  history: Inspection[] = [];
  query = '';
  sort: 'name' | 'score' = 'name';
  error = '';
  message = '';

  form = this.fb.nonNullable.group({
    inspection_date: ['', Validators.required],
    cleanliness_score: [5, [Validators.required, Validators.min(0), Validators.max(10)]],
    odor_score: [5, [Validators.required, Validators.min(0), Validators.max(10)]],
    waste_level: [5, [Validators.required, Validators.min(0), Validators.max(10)]],
    status: ['Good' as Inspection['status'], Validators.required],
    remarks: [''],
  });

  ngOnInit(): void {
    this.service.list().subscribe({
      next: (rows) => (this.facilities = rows),
      error: () => (this.error = 'Could not load facilities'),
    });
  }

  get average(): number {
    if (!this.facilities.length) return 0;
    return this.facilities.reduce((s, f) => s + f.cleanliness_score, 0) / this.facilities.length;
  }

  get needsAttention(): number {
    return this.facilities.filter((f) => f.cleanliness_score < 6).length;
  }

  get visible(): Facility[] {
    const q = this.query.trim().toLowerCase();
    let rows = this.facilities.filter(
      (f) =>
        !q ||
        f.name.toLowerCase().includes(q) ||
        f.location.toLowerCase().includes(q)
    );
    rows = [...rows].sort((a, b) =>
      this.sort === 'name'
        ? a.name.localeCompare(b.name)
        : a.cleanliness_score - b.cleanliness_score
    );
    return rows;
  }

  select(facility: Facility): void {
    this.selected = facility;
    this.error = '';
    this.message = '';
    this.service.history(facility.id).subscribe((rows) => (this.history = rows));
  }

  submit(): void {
    if (!this.selected || this.form.invalid) return;
    const payload: Inspection = {
      facility_id: this.selected.id,
      ...this.form.getRawValue(),
    };
    this.service.addInspection(payload).subscribe({
      next: (row) => {
        this.history = [row, ...this.history];
        this.message = 'Inspection saved.';
        this.form.patchValue({ remarks: '' });
      },
      error: () => (this.error = 'API could not save inspection.'),
    });
  }
}
