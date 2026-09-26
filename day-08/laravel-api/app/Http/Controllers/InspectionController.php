<?php

namespace App\Http\Controllers;

use App\Models\Inspection;
use Illuminate\Http\Request;
use Illuminate\Http\JsonResponse;

class InspectionController extends Controller
{
    public function index(Request $request): JsonResponse
    {
        $query = Inspection::with('facility')->orderByDesc('inspection_date');
        if ($request->filled('facility_id')) {
            $query->where('facility_id', $request->integer('facility_id'));
        }
        return response()->json($query->get());
    }

    public function store(Request $request): JsonResponse
    {
        $data = $request->validate([
            'facility_id' => 'required|exists:facilities,id',
            'inspection_date' => 'required|date',
            'cleanliness_score' => 'required|numeric|min:0|max:10',
            'odor_score' => 'required|numeric|min:0|max:10',
            'waste_level' => 'required|numeric|min:0|max:10',
            'status' => 'required|in:Good,Needs Attention,Poor',
            'remarks' => 'nullable|string',
        ]);

        $inspection = Inspection::create($data);
        return response()->json($inspection->load('facility'), 201);
    }

    public function show(int $id): JsonResponse
    {
        return response()->json(Inspection::with('facility')->findOrFail($id));
    }

    public function update(Request $request, int $id): JsonResponse
    {
        $inspection = Inspection::findOrFail($id);
        $data = $request->validate([
            'facility_id' => 'sometimes|exists:facilities,id',
            'inspection_date' => 'sometimes|date',
            'cleanliness_score' => 'sometimes|numeric|min:0|max:10',
            'odor_score' => 'sometimes|numeric|min:0|max:10',
            'waste_level' => 'sometimes|numeric|min:0|max:10',
            'status' => 'sometimes|in:Good,Needs Attention,Poor',
            'remarks' => 'nullable|string',
        ]);
        $inspection->update($data);
        return response()->json($inspection->fresh('facility'));
    }

    public function destroy(int $id): JsonResponse
    {
        Inspection::findOrFail($id)->delete();
        return response()->json(null, 204);
    }
}
