def minimum_distance(X, Y, Z):
    # Case 1: Construction is NOT between home and office
    if not ((0 < Y < X) or (X < Y < 0)):
        return abs(X)

    # Case 2: Construction is between home and office
    # Check if contractor is reachable
    if (0 < Y < Z) or (Z < Y < 0):
        return -1

    # Calculate total distance
    distance = abs(Z)              # Home -> Contractor
    distance += abs(Z - Y)          # Contractor -> Construction
    distance += abs(X - Y)          # Construction -> Office

    return distance






# ## 📌 Project Explanation: *Minimum Distance to Reach Office*

# This project solves a **real-life path planning problem** using basic logic.

# John lives on a straight road.

# * His **home** is at position `0`
# * His **office** is at position `X`
# * There is a **construction site** at position `Y` that blocks the road
# * The **contractor** who can stop the construction lives at position `Z`

# ---

# ## 🔍 Problem Logic (In Simple Words)

# * If there is **no construction between home and office**, John can go **directly** to the office.
# * If **construction blocks the way**, John **must first go to the contractor** to stop it.
# * After stopping construction, John can go to the office.
# * If the contractor is **on the other side of construction**, John **cannot reach** him → return `-1`.

# ---

# ## 🧠 What the Program Does

# 1. Checks if construction lies **between home (0) and office (X)**
# 2. If yes, checks whether the contractor is **reachable before construction**
# 3. Calculates **total distance traveled**:

#    * Home → Contractor
#    * Contractor → Construction
#    * Construction → Office
# 4. Returns:

#    * **Minimum distance** if possible
#    * **-1** if office cannot be reached

# ---

# ## ✅ Example (Simple)

# **Input:**

# ```
# Office (X) = 20  
# Construction (Y) = 10  
# Contractor (Z) = -10
# ```

# **Path:**
# Home → Contractor → Construction → Office
# **Total Distance = 40**

# ---

# ## ❌ When Output is -1

# If the contractor lives **beyond the construction**, John cannot reach him → **office unreachable**.

# ---

# ## 🎯 Key Concepts Used

# * Absolute distance calculation
# * Conditional logic
# * Edge case handling
# * Real-world problem modeling

# ---

# I
