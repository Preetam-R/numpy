"""
5 Classic NumPy Problems with Solutions
========================================
1. Array Creation & Reshaping
2. Broadcasting
3. Boolean Indexing & Filtering
4. Linear Algebra
5. Statistical Operations
"""

import numpy as np

print("=" * 60)
print("NUMPY PROBLEMS & SOLUTIONS")
print("=" * 60)

# ─────────────────────────────────────────────────────────
# Problem 1 — Array Creation & Reshaping
# ─────────────────────────────────────────────────────────
print("\n📌 Problem 1: Array Creation & Reshaping")
print("-" * 40)
print("Create a 1D array of integers 1–24.")
print("Reshape it into a 3D array of shape (2, 3, 4).")
print("Then transpose it so shape becomes (4, 3, 2).")

arr = np.arange(1, 25)
reshaped = arr.reshape(2, 3, 4)
transposed = reshaped.T

print("\n✅ Solution:")
print(f"  Original shape : {arr.shape}")
print(f"  After reshape  : {reshaped.shape}")
print(f"  After transpose: {transposed.shape}")
print(f"\n  Reshaped array:\n{reshaped}")


# ─────────────────────────────────────────────────────────
# Problem 2 — Broadcasting
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("📌 Problem 2: Broadcasting")
print("-" * 40)
print("Given a (4, 3) matrix, subtract the column-wise mean")
print("from each row WITHOUT using a loop.")

np.random.seed(42)
matrix = np.random.randint(10, 100, size=(4, 3))
col_mean = matrix.mean(axis=0)          # shape (3,)
normalized = matrix - col_mean          # broadcasts (4,3) - (3,)

print("\n✅ Solution:")
print(f"  Original matrix:\n{matrix}")
print(f"\n  Column means: {col_mean}")
print(f"\n  After subtracting column means:\n{normalized}")
print(f"\n  Verification — new column means: {normalized.mean(axis=0)}")


# ─────────────────────────────────────────────────────────
# Problem 3 — Boolean Indexing & Filtering
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("📌 Problem 3: Boolean Indexing & Filtering")
print("-" * 40)
print("From an array of 20 random integers (0–50),")
print("replace all values greater than 30 with -1,")
print("and count how many were replaced.")

np.random.seed(7)
data = np.random.randint(0, 51, size=20)
original = data.copy()

mask = data > 30
count_replaced = mask.sum()
data[mask] = -1

print("\n✅ Solution:")
print(f"  Original : {original}")
print(f"  Modified : {data}")
print(f"  Values replaced (>30 → -1): {count_replaced}")


# ─────────────────────────────────────────────────────────
# Problem 4 — Linear Algebra
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("📌 Problem 4: Linear Algebra")
print("-" * 40)
print("Solve the system of equations:")
print("  2x + 3y =  8")
print("  5x -  y = -2")
print("Then verify by computing A @ x = b.")

A = np.array([[2, 3],
              [5, -1]], dtype=float)
b = np.array([8, -2], dtype=float)

solution = np.linalg.solve(A, b)
verification = A @ solution

print("\n✅ Solution:")
print(f"  x = {solution[0]:.4f},  y = {solution[1]:.4f}")
print(f"  Verification A @ [x, y] = {verification}  (should be {b})")
print(f"  Determinant of A: {np.linalg.det(A):.2f}")


# ─────────────────────────────────────────────────────────
# Problem 5 — Statistical Operations
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("📌 Problem 5: Statistical Operations")
print("-" * 40)
print("Given exam scores for 5 students across 4 subjects,")
print("compute: per-student average, per-subject average,")
print("top scorer per subject, and overall pass rate (>=50).")

scores = np.array([
    [72, 85, 60, 90],
    [45, 55, 70, 40],
    [88, 92, 95, 78],
    [33, 48, 52, 61],
    [67, 74, 80, 55],
])
subjects = ['Math', 'Science', 'English', 'History']
students = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']

student_avg  = scores.mean(axis=1)
subject_avg  = scores.mean(axis=0)
top_scorers  = scores.argmax(axis=0)
pass_rate    = (scores >= 50).mean() * 100

print("\n✅ Solution:")
print(f"\n  Scores matrix (rows=students, cols=subjects):\n{scores}")
print("\n  Per-student averages:")
for name, avg in zip(students, student_avg):
    print(f"    {name:6s}: {avg:.1f}")
print("\n  Per-subject averages:")
for sub, avg in zip(subjects, subject_avg):
    print(f"    {sub:8s}: {avg:.1f}")
print("\n  Top scorer per subject:")
for sub, idx in zip(subjects, top_scorers):
    print(f"    {sub:8s}: {students[idx]} ({scores[idx, subjects.index(sub)]})")
print(f"\n  Overall pass rate (score >= 50): {pass_rate:.1f}%")

print("\n" + "=" * 60)
print("All 5 problems solved!")
print("=" * 60)