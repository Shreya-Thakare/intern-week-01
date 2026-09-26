<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Inspection extends Model
{
    protected $fillable = [
        'facility_id',
        'inspection_date',
        'cleanliness_score',
        'odor_score',
        'waste_level',
        'status',
        'remarks',
    ];

    protected $casts = [
        'inspection_date' => 'date',
        'cleanliness_score' => 'float',
        'odor_score' => 'float',
        'waste_level' => 'float',
    ];

    public function facility(): BelongsTo
    {
        return $this->belongsTo(Facility::class);
    }
}
