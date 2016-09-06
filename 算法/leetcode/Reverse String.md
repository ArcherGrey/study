# Reverse String
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

Subscribe to see which companies asked this question

    class Solution {
    public:
    	string reverseString(string s) {
    		string b = s;
    		b.replace(b.begin(),b.end(),s.rbegin(),s.rend());
    		return b;
    
    	}
    };