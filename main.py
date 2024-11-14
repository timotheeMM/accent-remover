import unicodedata

def remove_accents(input_str):
    # Normalize the string to decompose accented characters
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    # Filter out the non-ASCII characters
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    content_without_accents = remove_accents(content)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content_without_accents)

if __name__ == "__main__":
    input_file = './input.txt'  # place the file to be processed in the src folder and replace "input" with the name of your text file.
    output_file = 'output.txt'  # replace with the output location you want 

    process_file(input_file, output_file)
    print(f"Les accents ont été enlevés et le résultat a été écrit dans {output_file}")
