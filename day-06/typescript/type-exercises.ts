/**
 * Day 6 TypeScript exercises
 * Covers interfaces, enums, generics, type guards, unions
 */
import {
  Employee,
  EmploymentStatus,
  ApiResponse,
  filterByKeyword,
  computeMetrics,
  isEmployee,
  formatEmployee,
  SortKey,
} from './employee-types';

const sample: Employee[] = [
  {
    id: 1,
    name: 'Asha Patil',
    email: 'asha@example.com',
    department: 'Engineering',
    position: 'Developer',
    salary: 65000,
    status: EmploymentStatus.Active,
  },
  {
    id: 2,
    name: 'Ravi Shah',
    email: 'ravi@example.com',
    department: 'HR',
    position: 'Executive',
    salary: 48000,
    status: EmploymentStatus.Active,
  },
  {
    id: 3,
    name: 'Neha Joshi',
    email: 'neha@example.com',
    department: 'Engineering',
    position: 'QA Engineer',
    salary: 58000,
    status: EmploymentStatus.OnLeave,
  },
];

function sortEmployees(items: Employee[], key: SortKey, dir: 'asc' | 'desc' = 'asc'): Employee[] {
  const copy = [...items];
  copy.sort((a, b) => {
    const av = a[key];
    const bv = b[key];
    if (av < bv) return dir === 'asc' ? -1 : 1;
    if (av > bv) return dir === 'asc' ? 1 : -1;
    return 0;
  });
  return copy;
}

function wrapApi<T>(data: T, ok = true, message?: string): ApiResponse<T> {
  return { data, ok, message };
}

console.log('--- Metrics ---');
console.log(computeMetrics(sample));

console.log('--- Filter Engineering ---');
console.log(filterByKeyword(sample, 'eng').map(formatEmployee));

console.log('--- Sort by salary desc ---');
console.log(sortEmployees(sample, 'salary', 'desc').map(formatEmployee));

console.log('--- Type guard ---');
console.log(isEmployee(sample[0]), isEmployee({ foo: 1 }));

console.log('--- API wrapper ---');
console.log(wrapApi(sample[0]));
