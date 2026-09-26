<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\FacilityController;
use App\Http\Controllers\InspectionController;
use App\Http\Controllers\ComplaintController;

/*
| API routes — mount under /api (RouteServiceProvider / bootstrap)
| Flow: Request → Route → Controller → Model → Database → Response
*/

Route::apiResource('facilities', FacilityController::class);
Route::apiResource('inspections', InspectionController::class);
Route::apiResource('complaints', ComplaintController::class);

// Nested convenience route used by Day 9 Angular dashboard
Route::get('facilities/{facility}/inspections', function (int $facility) {
    return \App\Models\Inspection::where('facility_id', $facility)
        ->orderByDesc('inspection_date')
        ->get();
});
