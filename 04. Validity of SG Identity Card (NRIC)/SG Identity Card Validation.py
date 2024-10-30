# Alphabet look-up tables for S, T, F or G status of the holder to map check digit (0-10)
# "S": Singapore Citizens and permanent residents born before 1 Jan 2000
# "T": Singapore Citizens and permanent residents born on or after 1 Jan 2000
# "F": Foreigners holding long-term passes before 1 Jan 2000
# "G": Foreigners holding long-term passes on or after 1 Jan 2000
alphabet_table_s = {0: "J", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "Z"}
alphabet_table_t = {0: "G", 1: "H", 2: "I", 3: "Z", 4: "J", 5: "A", 6: "B", 7: "C", 8: "D", 9: "E", 10: "F"}
alphabet_table_f = {0: "X", 1: "K", 2: "L", 3: "M", 4: "N", 5: "P", 6: "Q", 7: "R", 8: "T", 9: "U", 10: "W"}
alphabet_table_g = {0: "R", 1: "T", 2: "U", 3: "W", 4: "X", 5: "K", 6: "L", 7: "M", 8: "N", 9: "P", 10: "Q"}


def checksum(nric_number):
    """Checksum of the first 7 digits of the given NRIC number."""
    weights = [2, 7, 6, 5, 4, 3, 2] #NRIC weight table for computing the checksum
    sum_of_products = sum(int(digit) * weight for digit, weight in zip(nric_number, weights))
    remainder = sum_of_products % 11
    checksum = 11 - remainder if remainder != 0 else 0  
    return checksum


def check_last_letter(check_digit, nric_type):
    """
    Get the corresponding alphabet based on the alphabet look-up table.
    This function retrieves the corresponding alphabet from the look-up table based on NRIC types (S, T, F, G)
    and computed check digit. 
    """
    if nric_type == "S":
        alphabet_table = alphabet_table_s
    elif nric_type == "T":
        alphabet_table = alphabet_table_t
    elif nric_type == "F":
        alphabet_table = alphabet_table_f
    elif nric_type == "G":
        alphabet_table = alphabet_table_g
    else:
        return "Invalid NRIC" #If the check digit is not valid (not between 0 and 10)
    
    return alphabet_table.get(check_digit, "Invalid NRIC")


def validate_nric(nric_number):
    """Validate NRIC number."""
    if len(nric_number) != 9 or not nric_number[0].upper() in ['S', 'T', 'F', 'G'] or not nric_number[1:8].isdigit(): #Check format
        return False

    #Calculates check digit from first 7 digits and fetches expected alphabet using check_last_letter function
    checksum_result = checksum(nric_number[1:8]) 
    expected_alphabet = check_last_letter(checksum_result, nric_number[0].upper())
    
    return expected_alphabet == nric_number[-1].upper()


def main():
    nric_number = input("Please enter your NRIC number (S, T, F, or G + 7 digits + alphabet): ")
    is_valid = validate_nric(nric_number)
    masked_nric = '*' * 5 + nric_number[5:]
    print(f"NRIC number {masked_nric} is valid: {is_valid}")

if __name__ == "__main__":
    main()
