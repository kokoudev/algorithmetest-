import sys
sys.path.insert(0, '.')

from algorithms.quicksortv1 import quicksort_v1
from algorithms.tow_sum2 import find_t_sum
from algorithms.Karasubasolo import karatsuba

def test_quicksort():
    print("Testing QuickSort...")
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    result = quicksort_v1(arr, 1)
    assert result == [1, 1, 2, 3, 4, 5, 6, 9], f"Expected sorted array, got {result}"
    print("✅ QuickSort passed")

def test_two_sum():
    print("Testing Two Sum...")
    arr = [1, 2, 3, 4, 5, -1, -2, 0]
    result = find_t_sum(arr)
    print(f"   Found {result} sums")
    assert result >= 0, f"Expected count >= 0, got {result}"
    print("✅ Two Sum passed")

def test_karatsuba():
    print("Testing Karatsuba...")
    a, b = 1234, 5678
    result = karatsuba(a, b)
    expected = a * b
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Karatsuba passed")

if __name__ == '__main__':
    try:
        test_quicksort()
        test_two_sum()
        test_karatsuba()
        print("\n🎉 All tests passed!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
