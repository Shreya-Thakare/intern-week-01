import './globals.css';
import Link from 'next/link';

export const metadata = {
  title: 'Employee Dashboard · Day 7',
  description: 'Next.js + Node.js employee management',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div className="shell">
          <nav className="nav">
            <Link href="/employees" className="nav-brand">
              Day 7 · Employee API Dashboard
            </Link>
            <div className="nav-links">
              <Link href="/employees">Employees</Link>
              <Link href="/employees/create">Create</Link>
            </div>
          </nav>
          {children}
        </div>
      </body>
    </html>
  );
}
