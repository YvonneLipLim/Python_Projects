# Validity of Singapore Identity Card (NRIC/FIN)

The validation program is coded in Python and validates the Singapore NRIC/FIN number with the initial letter of S, T, F, G or M, depending on the status of the holder, followed by the seven (7) digits and one letter behind.
* Singapore citizens and permanent residents born before 1 January 2000 are assigned the letter "S".
* Singapore citizens and permanent residents born on or after 1 January 2000 are assigned the letter "T".
* Foreigners issued with long-term passes before 1 January 2000 are assigned the letter "F".
* Foreigners issued with long-term passes from 1 January 2000 to 31 December 2021 are assigned the letter "G".
* Foreigners issued with long-term passes on or after 1 January 2022 are assigned the letter "M".

The last letter is obtained from the seven (7) digits using the modules eleven method which is computed as follows:
1. Each digit in the NRIC/FIN number is multiplied by its weight as shown below:
    <img src="https://github.com/YvonneLipLim/Images/blob/main/NRIC_Weight_Table.png">
2. Add together NRIC/FIN x WEIGHT products.
3. Add 4 to SUM if the initial letter is "G" or "T", add 3 to SUM if the initial letter is "M".
4. Divide the result SUM by 11 to get the value of the REEMAINDER.
5. ADD 1 to the REMAINDER AND SUBTRACT it from 11 to get CHECK DIGIT.
    <img src="https://github.com/YvonneLipLim/Images/blob/main/CheckSum.png">
  
6. Use CHECK DIGIT to get CHECKSUM from the below corresponding letter table:
   
    <img src="https://github.com/YvonneLipLim/Images/blob/main/Letter_Table.png">
<br>
