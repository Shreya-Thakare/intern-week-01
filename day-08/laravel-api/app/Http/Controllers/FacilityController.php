<?php

namespace App\Http\Controllers;

use App\Models\Facility;
use Illuminate\Http\Request;
use Illuminate\Http\JsonResponse;

class FacilityController extends Controller
{
    public function index(): JsonResponse
    {
        return response()->json(Facility::withCount(['inspections', 'complaints'])->orderBy('name')->get());
    }

    public function store(Request $request): JsonResponse
    {
        $data = $request->validate([
            'name' => 'required|string|max:150',
            'location' => 'required|string|max:150',
            'cleanliness_score' => 'nullable|numeric|min:0|max:10',
            'water_availability' => 'boolean',
        ]);

        $facility = Facility::create($data);
        return response()->json($facility, 201);
    }

    public function show(int $id): JsonResponse
    {
        $facility = Facility::with(['inspections', 'complaints'])->findOrFail($id);
        return response()->json($facility);
    }

    public function update(Request $request, int $id): JsonResponse
    {
        $facility = Facility::findOrFail($id);
        $data = $request->validate([
            'name' => 'sometimes|required|string|max:150',
            'location' => 'sometimes|required|string|max:150',
            'cleanliness_score' => 'nullable|numeric|min:0|max:10',
            'water_availability' => 'boolean',
        ]);
        $facility->update($data);
        return response()->json($facility);
    }

    public function destroy(int $id): JsonResponse
    {
        Facility::findOrFail($id)->delete();
        return response()->json(null, 204);
    }
}
