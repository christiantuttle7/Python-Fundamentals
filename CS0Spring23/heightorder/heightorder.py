# Corin Chepko
# 3/8/23
# Kattis:Height order https://open.kattis.com/problems/height
# Algorithm steps:
# 1.) input n for number of folowing line
# 2.) input a line of text and turn it into a list of numbers
# 3.) cycle through list, if we see a number greater than the last, the students step back

def main():
    n_line = int(input())

    for line in range(n_line):
        
        in_list = list(map(int, input().split()))
        k = in_list[0]
        order_list = []
        order_list.append(in_list[1])
        students = in_list[2::]

        steps=0
        for stud in students:
            added=False
            index=0
            for s in order_list:
                if(stud < s):
                    steps = steps + len(order_list[index::])
                    order_list.insert(index, stud)
                    added = True
                    break
                index += 1
            if(not added):
                order_list.append(stud)

        
        #print(order_list)
        print(f"{k} {steps}")

if __name__ == "__main__":
    main()