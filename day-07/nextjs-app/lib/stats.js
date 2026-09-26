/** Build visualization stats from employee dataset */
export function buildStats(employees) {
  const total = employees.length;
  const salaries = employees.map((e) => Number(e.salary) || 0);
  const sum = salaries.reduce((a, b) => a + b, 0);
  const avg = total ? sum / total : 0;
  const max = total ? Math.max(...salaries) : 0;
  const min = total ? Math.min(...salaries) : 0;
  const top = total
    ? employees.reduce((a, b) => (Number(a.salary) >= Number(b.salary) ? a : b))
    : null;

  const byDept = {};
  employees.forEach((e) => {
    const d = e.department || 'Other';
    if (!byDept[d]) byDept[d] = { count: 0, totalSalary: 0 };
    byDept[d].count += 1;
    byDept[d].totalSalary += Number(e.salary) || 0;
  });

  const deptStats = Object.entries(byDept)
    .map(([name, v]) => ({
      name,
      count: v.count,
      avg: v.totalSalary / v.count,
      total: v.totalSalary,
    }))
    .sort((a, b) => b.avg - a.avg);

  const bands = [
    { name: '< ₹40k', min: 0, max: 40000, count: 0 },
    { name: '₹40–60k', min: 40000, max: 60000, count: 0 },
    { name: '₹60–80k', min: 60000, max: 80000, count: 0 },
    { name: '≥ ₹80k', min: 80000, max: Infinity, count: 0 },
  ];
  salaries.forEach((s) => {
    const b = bands.find((x) => s >= x.min && s < x.max);
    if (b) b.count += 1;
  });

  return { total, avg, max, min, top, deptStats, bands };
}
