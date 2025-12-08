# Snake Scales (Chapter 1)

This problem shares similarities with chapter 2. Here in chapter 1, the ground cannot be used. Solid Snake is back at work scaling Metal Platforms! This time, he is bringing his own ladder. Solid Snake needs to inspect N platforms, numbered 
1 to N. The i-th platform is a horizontal line segment from points (i,Ai) to (i+1,Ai), inclusive. Solid Snake starts on platform 1. He can travel between two platforms with a ladder of height h or greater if there exists a vertical line segment of length h that intersects both platforms.
Metal Platforms Inc. has tasked you to write a program, "Scale AI", to find the length of the shortest ladder that Solid Snake needs to visit each platform at least once, starting from platform 1.

# Constraints
1≤T≤65 </br>
1≤N≤100 </br>
1≤Ai≤100 </br>

# Input Format
Input begins with a single integer T, the number of test cases. The first line of each case is a single integer N. The second line of each case contains N space-separated integers A1, ..., AN.

# Output Format
For the i-th test case, print "Case #i: " followed by the length of the shortest ladder that Solid Snake needs to visit each platform at least once.
Sample Explanation
In the first sample case, there are N=5 platforms with heights A=[2,4,5,1,4] respectively. To be able to access all the platforms, Solid Snake needs a ladder of at least height 4, with potential placements shown below.

# Sample Input
6 </br>
5 </br>
2 4 5 1 4 </br>
3 </br>
13 10 11 </br>
4 </br>
1 3 3 7 </br>
1 </br>
42 </br>
3 </br>
5 50 42 </br>
7 </br>
4 2 5 6 4 2 1 </br>

# Sample Output
Case #1: 4 </br>
Case #2: 3 </br>
Case #3: 4 </br>
Case #4: 0 </br>
Case #5: 45 </br>
Case #6: 3 </br>
