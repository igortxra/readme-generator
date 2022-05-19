DATA = {
    "$SERVICE": "",
    "$SHORT_DESCRIPTION": '',
    "$WHAT_IT_DOES": '',
    "$FUNCTION_NAME": '',
    "$HTTP_METHOD": ''
}

for key, value in DATA.items():
    DATA[key] = input(f"Digite o {key[1:]}: ")


# Read in the file
with open('GCF_TEMPLATE.md', 'r', encoding='utf-8') as file:
    filedata = file.read()

# Replace the target string
for k, v in DATA.items():
    filedata = filedata.replace(k, v)

# Write the file out again
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(filedata)
