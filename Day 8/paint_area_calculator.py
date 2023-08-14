def paint_calc(height, width, coverage):
    area = height * width
    no_of_cans = area / coverage
    cans = round(no_of_cans)
    return cans


test_h = int(input("Height of wall : "))
test_w = int(input("Width of wall : "))
coverage = 5
cans = paint_calc(test_h,test_w,coverage)

print(f"For a wall of height = {test_h} and width = {test_w}, it would require {cans} cans to paint it completely, given that 1 can covers {coverage} blocks.")