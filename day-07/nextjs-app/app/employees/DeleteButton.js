'use client';

import { useRouter } from 'next/navigation';
import { useState } from 'react';
import { deleteEmployee } from '../../lib/api';

export default function DeleteButton({ id, name }) {
  const router = useRouter();
  const [busy, setBusy] = useState(false);

  async function onDelete() {
    if (!confirm(`Delete ${name}?`)) return;
    setBusy(true);
    try {
      await deleteEmployee(id);
      router.refresh();
    } catch (err) {
      alert(err.message);
      setBusy(false);
    }
  }

  return (
    <button
      type="button"
      className="btn btn-danger btn-sm"
      onClick={onDelete}
      disabled={busy}
    >
      {busy ? '…' : 'Delete'}
    </button>
  );
}
