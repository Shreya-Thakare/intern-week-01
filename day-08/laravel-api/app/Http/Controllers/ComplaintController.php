<?php

namespace App\Http\Controllers;

use App\Models\Complaint;
use Illuminate\Http\Request;
use Illuminate\Http\JsonResponse;

class ComplaintController extends Controller
{
    public function index(Request $request): JsonResponse
    {
        $query = Complaint::with('facility')->orderByDesc('created_at');
        if ($request->filled('facility_id')) {
            $query->where('facility_id', $request->integer('facility_id'));
        }
        if ($request->filled('status')) {
            $query->where('status', $request->string('status'));
        }
        return response()->json($query->get());
    }

    public function store(Request $request): JsonResponse
    {
        $data = $request->validate([
            'facility_id' => 'required|exists:facilities,id',
            'description' => 'required|string',
            'status' => 'nullable|in:Open,In Progress,Resolved',
        ]);
        $data['status'] = $data['status'] ?? 'Open';
        $complaint = Complaint::create($data);
        return response()->json($complaint->load('facility'), 201);
    }

    public function show(int $id): JsonResponse
    {
        return response()->json(Complaint::with('facility')->findOrFail($id));
    }

    public function update(Request $request, int $id): JsonResponse
    {
        $complaint = Complaint::findOrFail($id);
        $data = $request->validate([
            'facility_id' => 'sometimes|exists:facilities,id',
            'description' => 'sometimes|required|string',
            'status' => 'sometimes|in:Open,In Progress,Resolved',
        ]);
        $complaint->update($data);
        return response()->json($complaint->fresh('facility'));
    }

    public function destroy(int $id): JsonResponse
    {
        Complaint::findOrFail($id)->delete();
        return response()->json(null, 204);
    }
}
