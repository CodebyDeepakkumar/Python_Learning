# if __name__ == '__main__':
#     tot = 0
    
#     percentage = 0
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
    
    
#     for marks in student_marks[query_name]:
    
#         tot += marks
#         percentage = tot / n
#         formatted_percentage = "{:.2}".format(percentage)
        
        
        


#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

# def print_full_name(first, last):
#     return f"Hello {first}{last}! You just delved into Python."
   
#     # Write your code here

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

learn_string = '1234567890'
print(learn_string[:5])