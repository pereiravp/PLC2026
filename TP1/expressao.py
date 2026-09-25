## Código Gerado pelo regex101

import re

pattern = re.compile(r"^1*(0+1)*0*$", flags=re.MULTILINE)

test_string = ("10101\n"
	"0101\n"
	"0110\n"
	"0011\n"
	"010101010000\n"
	"1110001010\n"
	"0001\n"
	"101011\n\n"
	"01110\n"
	"1110\n"
	"000\n")

matches = pattern.finditer(test_string)

for match_num, match in enumerate(matches, start=1):
    print(f"Match {match_num} was found at {match.start()}-{match.end()}: {match.group()}")

    for group_num, group in enumerate(match.groups(), start=1):
        print(f"Group {group_num} found at {match.start(group_num)}-{match.end(group_num)}: {group}")
