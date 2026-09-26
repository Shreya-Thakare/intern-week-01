'use client';

import { useEffect, useState } from 'react';
import { money } from '../../lib/api';

const COLORS = ['#3b82f6', '#22c55e', '#a78bfa', '#f59e0b', '#ef4444', '#06b6d4', '#ec4899'];

export default function Charts({ stats }) {
  const [ready, setReady] = useState(false);
  useEffect(() => {
    const t = requestAnimationFrame(() => setReady(true));
    return () => cancelAnimationFrame(t);
  }, []);

  if (!stats || !stats.total) {
    return <p className="muted">No data to visualize. Start the API or add employees.</p>;
  }

  const { deptStats, bands, total } = stats;
  const maxAvg = Math.max(...deptStats.map((d) => d.avg), 1);
  const maxBand = Math.max(...bands.map((b) => b.count), 1);

  // Donut geometry
  const r = 52;
  const c = 2 * Math.PI * r;
  let offset = 0;
  const slices = deptStats.map((s, i) => {
    const frac = s.count / total;
    const len = frac * c;
    const slice = {
      name: s.name,
      count: s.count,
      pct: Math.round(frac * 100),
      color: COLORS[i % COLORS.length],
      dash: `${len} ${c - len}`,
      offset: -offset,
    };
    offset += len;
    return slice;
  });

  return (
    <div className="charts-grid">
      <div>
        <h3 className="chart-title">Average salary by department</h3>
        <div className="bar-chart">
          {deptStats.map((s) => {
            const pct = Math.round((s.avg / maxAvg) * 100);
            return (
              <div className="bar-row" key={s.name}>
                <span className="bar-label" title={s.name}>{s.name}</span>
                <div className="bar-track">
                  <div
                    className="bar-fill"
                    style={{ width: ready ? `${pct}%` : '0%' }}
                  />
                </div>
                <span className="bar-num">{money(s.avg)}</span>
              </div>
            );
          })}
        </div>
      </div>

      <div>
        <h3 className="chart-title">Headcount by department</h3>
        <div className="donut-wrap">
          <div className="donut">
            <svg viewBox="0 0 120 120" aria-hidden="true">
              <circle cx="60" cy="60" r={r} fill="none" stroke="#1c2738" strokeWidth="12" />
              {slices.map((s) => (
                <circle
                  key={s.name}
                  cx="60"
                  cy="60"
                  r={r}
                  fill="none"
                  stroke={s.color}
                  strokeWidth="12"
                  strokeDasharray={s.dash}
                  strokeDashoffset={s.offset}
                  transform="rotate(-90 60 60)"
                />
              ))}
            </svg>
            <div className="donut-center">
              <strong>{total}</strong>
              <span>people</span>
            </div>
          </div>
          <div className="legend">
            {slices.map((s) => (
              <div className="legend-item" key={s.name}>
                <span className="swatch" style={{ background: s.color }} />
                {s.name} · {s.count} ({s.pct}%)
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="full">
        <h3 className="chart-title">Salary band distribution</h3>
        <div className="bar-chart">
          {bands.map((b) => {
            const pct = Math.round((b.count / maxBand) * 100);
            return (
              <div className="bar-row" key={b.name}>
                <span className="bar-label">{b.name}</span>
                <div className="bar-track">
                  <div
                    className="bar-fill band"
                    style={{ width: ready ? `${pct}%` : '0%' }}
                  />
                </div>
                <span className="bar-num">{b.count}</span>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
