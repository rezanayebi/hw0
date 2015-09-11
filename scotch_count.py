##################
# Reza Nayebi
# rn2324
# scotch_count.py
#################


if __name__ == "__main__":
    drinks_csv = open("iowa-liquor-sample.csv")
    liquor_name = "single malt scotch"
    count = 0
    for line in drinks_csv:
        if liquor_name in line.lower():
            count += 1
    drinks_csv.close()
    print count



