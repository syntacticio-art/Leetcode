📘 Simple Explanation of the Code 

Imagine you have cities numbered from 1 to C, and some cities are connected by wires. You also get a list of queries that ask you two things:

Type 1: “Give me the smallest online city in the same group as city X.”

Type 2: “Turn city X offline.”

This code answers those questions fast.

🗺️ How it Works:

Think of each city as a house. Some houses have secret tunnels between them, forming groups. If you can reach one house in a group, you can reach all of them.

We use a smart system called DSU (Disjoint Set Union) to:

✅ Find which group a house belongs to
✅ Join houses into bigger groups

This is done using two magic tricks:

find(x): tells you the leader of x’s group

union(a, b): joins the groups of a and b

🧺 Keeping Track of the “Smallest Online City”

For each group of connected houses:

We make a min-heap (a basket that always gives the smallest number first).

Every city starts as online.

If a city goes offline, we remove it from the online set.

When someone asks:

❓ “Give me the smallest online house in City X’s group”

We:

Look at X’s group.

Check the heap for that group.

Remove any cities that are offline.

Return the smallest one left.

If none are left, return -1.

❓ “Turn off house X”

We simply mark it offline.

🧠 Final Summary (One Line)

The code groups connected cities, keeps each group in a min-heap, tracks which cities are online, and answers smallest-online-city queries efficiently.
