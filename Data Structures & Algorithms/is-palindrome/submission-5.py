class Solution:
    def isPalindrome(self, s: str) -> bool:

        text = "Hello, World! 123 #Python_2026."


        temp = "".join(char for char in s if char.isalnum()) 

        print(temp)


        l = len(temp)

        if l%2 == 0:

            mid = l//2

            print("mid variable ",mid)
            
            
            s1 = "".join(char for char in temp[0:mid])   
            s2 = "".join(char for char in temp[mid:len(temp)])
            revs2 = s2[::-1]

            print(s1)
            print(revs2) 

            if s1.lower() == revs2.lower():
                return True

            else:
                return False

        else:

            mid = l//2

            print("mid variable ",mid)
            
            
            s1 = "".join(char for char in temp[0:mid])   
            s2 = "".join(char for char in temp[mid+1:len(temp)])
            revs2 = s2[::-1]

            print(s1)
            print(revs2) 

            if s1.lower() == revs2.lower():
                return True

            else:
                return False


        