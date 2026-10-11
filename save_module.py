
import os


def save_analysis(analysis):

    os.makedirs("outputs",exist_ok=True)

    filename="outputs/legal_analysis.txt"

    with open(filename,"w",encoding="utf-8") as file:
        file.write("AUTOMATED LEGAL DOCUMENT ANALYSIS\n")
        file.write("="*40+"\n\n")
        file.write(analysis)

    return filename
