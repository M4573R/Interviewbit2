/*As said before, this problem does not allow using library functions.

What if you maintained the length of the current word?

You reset the length of the word when the next word begins (When does a new word begin?)

Return the last length you have.*/

class Solution {
    public:
        int lengthOfLastWord(const string &s) {
            int len = 0;
            while (*s) {  
                if (*s != ' ') {
                    len++;
                    s++;
                    continue;
                }
                s++;
                if (*s && *s != ' ') len = 0;
            }
            return len;

        }
};
