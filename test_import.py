import sys
import os

# Add the parent directory (job_bot/) to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from utils.cover_letter_generator import generate_cover_letter
    print("✅ Import successful!")
except ModuleNotFoundError as e:
    print("❌ Import failed:", e)
