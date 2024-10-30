# Validity of Singapore Identity Card (NRIC/FIN)

The validation program is coded in Python and validates the Singapore NRIC/FIN number with the initial letter of S, T, F or G, depending on the status of the holder, followed by the seven (7) digits and one letter behind.
* Singapore citizens and permanent residents born before 1 January 2000 are assigned the letter "S".
* Singapore citizens and permanent residents born on or after 1 January 2000 are assigned the letter "T".
* Foreigners issued with long-term passes before 1 January 2000 are assigned the letter "F".
* Foreigners issued with long-term passes from 1 January 2000 to 31 December 2021 are assigned the letter "G".

The last letter is obtained from the seven (7) digits using the modules eleven method which is computed as follows:
1. Each digit in the NRIC/FIN number is multiplied by its weight as shown below:
    <img src="https://github.com/YvonneLipLim/Images/blob/main/NRIC_Weight.png">
2. Add together NRIC/FIN x WEIGHT products.
3. Divide the result SUM by 11 to get the REMAINDER.
5. SUBTRACT REMAINDER from 11 to get CHECK DIGIT.
    <img src="https://github.com/YvonneLipLim/Images/blob/main/Checksum_Calculation.png">
  
6. Use CHECK DIGIT result to get CHECKSUM from the below corresponding letter table:
   
    <img src="https://github.com/YvonneLipLim/Images/blob/main/Checksum_Table.png">
<br>
