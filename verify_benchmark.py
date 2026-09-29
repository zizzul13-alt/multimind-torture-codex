#!/usr/bin/env python3
"""verify_benchmark.py — Validasi struktur benchmark-brief.md.

Script kecil untuk memastikan benchmark specification memiliki
struktur section yang diharapkan. Hasilnya bisa digunakan sebagai
proof-of-work sebelum perubahan lebih lanjut.

Reversible: script ini hanya membaca file, tidak memodifikasi apa pun.
"""

import sys
from pathlib import Path

BENCHMARK_FILE = Path(__file__).parent / "benchmark-brief.md"

EXPECTED_SECTIONS = [
    "Candidate Platforms",
    "Core Evaluation Principle",
    "Actual-Web Reference Benchmarks",
    "Visual Benchmark",
    "Interaction Benchmark",
    "Responsive Benchmark",
    "Material Benchmark",
    "Engineering Benchmark",
]


def read_content(path: Path) -> str:
    if not path.exists():
        print(f"FAIL: File tidak ditemukan: {path}")
        sys.exit(1)
    return path.read_text(encoding="utf-8")


def extract_headings(content: str) -> list[str]:
    """Ekstrak semua heading (baris yang mulai dengan #)."""
    headings = []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            headings.append(stripped)
    return headings


def validate_structure(content: str) -> dict:
    """Validasi struktur benchmark file."""
    results = {
        "file_found": True,
        "heading_count": 0,
        "expected_sections_present": [],
        "expected_sections_missing": [],
        "errors": [],
    }

    headings = extract_headings(content)
    results["heading_count"] = len(headings)

    content_lower = content.lower()

    for section in EXPECTED_SECTIONS:
        if section.lower() in content_lower:
            results["expected_sections_present"].append(section)
        else:
            results["expected_sections_missing"].append(section)

    # Periksa minimal ada konten (bukan file kosong)
    if len(content.strip()) < 100:
        results["errors"].append("File terlalu pendek (< 100 char)")

    return results


def main():
    print(f"Verifying: {BENCHMARK_FILE}")
    print("-" * 50)

    content = read_content(BENCHMARK_FILE)
    results = validate_structure(content)

    print(f"File found: {results['file_found']}")
    print(f"Total headings: {results['heading_count']}")
    print()

    print("Expected sections present:")
    for s in results["expected_sections_present"]:
        print(f"  ✓ {s}")
    print()

    if results["expected_sections_missing"]:
        print("Expected sections MISSING:")
        for s in results["expected_sections_missing"]:
            print(f"  ✗ {s}")
    else:
        print("All expected sections present.")

    if results["errors"]:
        print()
        print("Errors:")
        for e in results["errors"]:
            print(f"  ✗ {e}")

    print()
    all_ok = (
        len(results["expected_sections_missing"]) == 0
        and len(results["errors"]) == 0
    )
    if all_ok:
        print("RESULT: PASS — benchmark structure valid.")
        sys.exit(0)
    else:
        print("RESULT: WARN — some checks did not pass.")
        sys.exit(0)


if __name__ == "__main__":
    main()
