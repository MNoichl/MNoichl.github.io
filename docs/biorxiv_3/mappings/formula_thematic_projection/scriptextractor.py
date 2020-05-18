from bs4 import BeautifulSoup as bs

# Load the HTML content
file = input("File: ")

html_file = open(file, 'r')
html_content = html_file.read()
html_file.close() # clean up

# Initialize the BS object
soup  = bs(html_content,'html.parser') 
all_scripts = soup.body.find_all('script', recursive=False)
script_list = [len(str(x)) for x in all_scripts]

max_index=dict(zip(script_list,range(0,len(script_list)-1)))[max(script_list)]
print(max_index)
for counter,script in enumerate(all_scripts):

   # Print the src attribute
	f = open(str(counter)+'.js', "w")
	f.write(str(script))
	f.close()
	if counter == max_index:
		print('max_here:', counter)
		script.decompose()

with open("output1.html", "w") as file:
    file.write(str(soup))
