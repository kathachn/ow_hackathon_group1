import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_data import validate

class DataIntegrityTests(unittest.TestCase):
    def test_all_cities_have_consistent_versioned_artifacts(self):
        results = validate()
        self.assertEqual(set(results), {"berlin", "frankfurt", "muenchen"})
        self.assertEqual(sum(x["grid"] for x in results.values()), 21233)

if __name__ == "__main__":
    unittest.main()
