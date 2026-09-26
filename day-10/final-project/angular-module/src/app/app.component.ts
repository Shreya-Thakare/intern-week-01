import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

interface PredictResponse {
  hygiene_risk: 'High' | 'Low';
  high_risk_probability: number;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  template: `
    <main style="max-width:560px;margin:2rem auto;padding:1.25rem;background:#fff;border-radius:14px;box-shadow:0 1px 3px rgb(0 0 0 / 8%)">
      <small style="color:#64748b">DAY 10 • ANGULAR MODULE</small>
      <h1 style="margin:0.25rem 0 1rem">Hygiene Risk Predictor</h1>
      <p style="color:#475569">Functional Angular page connected to the FastAPI <code>/predict</code> endpoint.</p>

      <form [formGroup]="form" (ngSubmit)="submit()" style="display:grid;gap:0.6rem">
        <label>Cleanliness <input type="number" min="0" max="10" step="0.1" formControlName="cleanliness_score" /></label>
        <label>Odor <input type="number" min="0" max="10" step="0.1" formControlName="odor_score" /></label>
        <label>Waste <input type="number" min="0" max="10" step="0.1" formControlName="waste_level" /></label>
        <label>Complaints <input type="number" min="0" formControlName="complaints" /></label>
        <label>Footfall <input type="number" min="0" formControlName="footfall" /></label>
        <label>Hours since cleaning <input type="number" min="0" formControlName="hours_since_cleaning" /></label>
        <button type="submit" [disabled]="form.invalid || loading" style="padding:0.6rem;border:0;border-radius:8px;background:#2563eb;color:#fff;font-weight:600">
          {{ loading ? 'Predicting…' : 'Predict' }}
        </button>
      </form>

      <p *ngIf="result" style="margin-top:1rem">
        Risk: <strong>{{ result.hygiene_risk }}</strong>
        (probability {{ result.high_risk_probability }})
      </p>
      <p *ngIf="error" style="color:#dc2626">{{ error }}</p>
    </main>
  `,
})
export class AppComponent {
  private http = inject(HttpClient);
  private fb = inject(FormBuilder);

  loading = false;
  result: PredictResponse | null = null;
  error = '';

  form = this.fb.nonNullable.group({
    cleanliness_score: [5, [Validators.required, Validators.min(0), Validators.max(10)]],
    odor_score: [7, [Validators.required, Validators.min(0), Validators.max(10)]],
    waste_level: [6, [Validators.required, Validators.min(0), Validators.max(10)]],
    complaints: [4, [Validators.required, Validators.min(0)]],
    footfall: [350, [Validators.required, Validators.min(0)]],
    hours_since_cleaning: [24, [Validators.required, Validators.min(0)]],
  });

  submit(): void {
    if (this.form.invalid) return;
    this.loading = true;
    this.error = '';
    this.result = null;
    this.http
      .post<PredictResponse>('http://localhost:8000/predict', this.form.getRawValue())
      .subscribe({
        next: (res) => {
          this.result = res;
          this.loading = false;
        },
        error: () => {
          this.error = 'API unavailable. Start backend with: python backend/main.py';
          this.loading = false;
        },
      });
  }
}
