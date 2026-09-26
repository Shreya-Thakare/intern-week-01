<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('departments', function (Blueprint $table) {
            $table->id();
            $table->string('name')->unique();
            $table->timestamps();
        });

        Schema::create('employees', function (Blueprint $table) {
            $table->id();
            $table->foreignId('department_id')->constrained()->cascadeOnDelete();
            $table->string('name');
            $table->string('email')->unique();
            $table->decimal('salary', 10, 2);
            $table->timestamps();
        });

        Schema::create('facilities', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('location');
            $table->decimal('cleanliness_score', 4, 2)->nullable();
            $table->boolean('water_availability')->default(true);
            $table->timestamps();
        });

        Schema::create('inspections', function (Blueprint $table) {
            $table->id();
            $table->foreignId('facility_id')->constrained()->cascadeOnDelete();
            $table->date('inspection_date');
            $table->decimal('cleanliness_score', 4, 2);
            $table->decimal('odor_score', 4, 2);
            $table->decimal('waste_level', 4, 2);
            $table->enum('status', ['Good', 'Needs Attention', 'Poor']);
            $table->text('remarks')->nullable();
            $table->timestamps();
            $table->index(['facility_id', 'inspection_date']);
        });

        Schema::create('complaints', function (Blueprint $table) {
            $table->id();
            $table->foreignId('facility_id')->constrained()->cascadeOnDelete();
            $table->text('description');
            $table->enum('status', ['Open', 'In Progress', 'Resolved'])->default('Open');
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('complaints');
        Schema::dropIfExists('inspections');
        Schema::dropIfExists('facilities');
        Schema::dropIfExists('employees');
        Schema::dropIfExists('departments');
    }
};
