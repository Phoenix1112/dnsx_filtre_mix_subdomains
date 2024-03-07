import os
import sys
import re
import argparse
import tldextract

def start_program():
	total_list = []

	try:

		open_file = open(args.list, "r").read().split("\n")
		file_file = list(set(filter(None, open_file)))
		file_file.sort()

		del open_file
		if len(file_file) == 0:
			print("subdomain listen boş")
			sys.exit()

		for i in file_file:
			if i:
				domain = tldextract.extract(i).registered_domain
				if domain not in total_list:
					total_list.append(domain)

	except:
		pass


	total_list = list(set(total_list))
	total_list.sort()

	for i in total_list:
		regex = f"(^{re.escape(i)}$|.*\.{re.escape(i)}$)"
		compile_regex = re.compile(regex)
		new = list(filter(compile_regex.match,file_file))
		with open("deneniyor.txt", "w") as file:
			for wr in new:
				file.write(wr + "\n")

		os.system(f"dnsx -l deneniyor.txt -wd {i} -a -cname -silent | tee -a {args.output}")
		os.system("rm deneniyor.txt")


if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-l", "--list", metavar="", required=True, help="Subdomain List")
    ap.add_argument("-o", "--output", metavar="", required=False, default="final_subdomains.txt",help="Save Output(Default:final_subdomains.txt)")
    args = ap.parse_args()

    start_program()
