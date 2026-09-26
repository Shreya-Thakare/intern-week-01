/** Day 6 — TypeScript types, interfaces, unions, enums, generics */

export type Department = 'Engineering' | 'HR' | 'Finance' | 'Operations' | 'Sales';

export enum EmploymentStatus {
  Active = 'Active',
  OnLeave = 'OnLeave',
  Inactive = 'Inactive',
}

export interface Employee {
  id: number;
  name: string;
  email: string;
  department: Department | string;
  position: string;
  salary: number;
  status?: EmploymentStatus;
  joinedAt?: string;
}

export type EmployeeFormData = Omit<Employee, 'id'> & { id?: number };

export type SortKey = 'name' | 'department' | 'salary' | 'id';
export type SortDir = 'asc' | 'desc';

export interface DashboardMetrics {
  total: number;
  averageSalary: number;
  departments: string[];
}

export interface ApiResponse<T> {
  data: T;
  ok: boolean;
  message?: string;
}

/** Type guard */
export function isEmployee(value: unknown): value is Employee {
  if (!value || typeof value !== 'object') return false;
  const e = value as Record<string, unknown>;
  return (
    typeof e.id === 'number' &&
    typeof e.name === 'string' &&
    typeof e.salary === 'number'
  );
}

/** Generic list helper */
export function filterByKeyword<T extends { name: string; department?: string }>(
  items: T[],
  keyword: string
): T[] {
  const q = keyword.trim().toLowerCase();
  if (!q) return items;
  return items.filter(
    (item) =>
      item.name.toLowerCase().includes(q) ||
      (item.department ?? '').toLowerCase().includes(q)
  );
}

export function formatEmployee(employee: Employee): string {
  return `${employee.name} (${employee.department}) — ₹${employee.salary.toLocaleString()}`;
}

export function computeMetrics(employees: Employee[]): DashboardMetrics {
  const total = employees.length;
  const averageSalary =
    total === 0
      ? 0
      : Math.round(employees.reduce((s, e) => s + e.salary, 0) / total);
  const departments = [...new Set(employees.map((e) => e.department))];
  return { total, averageSalary, departments };
}
