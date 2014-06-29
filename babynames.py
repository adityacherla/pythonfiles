#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the function extract_names below and change the calling
of the function in the main method

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  text = ''
  try: 
   with open(filename, 'r') as f:
    text = f.read()
  except IOError as err:
   print 'File Error: ',str(err)
  names = []
  names_ranks = {}
  #This regex here searches here for the year for which the names are listed
  match = re.search('Popularity in\\s\\d{4}',text) 
  if match:
   year = match.group().strip()
  else:
  #If it doesnt find any such text in the html files then the program exits
   print("Could not find any year to publish!") 
   sys.exit(1) 
  match = re.search(r'\d{4}',year)   #The search only the one complete match from the string that is the first one
  names.append(match.group().strip())
  #This regex searches all the names of boys and girls in the list and orders into tuples
  #The findall function gives all the mathces in text which are relevant to the search
  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',text) #The findall function return all the matched string in tuples
  for entrys in tuples:
   (rank,boyname,girlname)= entrys
   if boyname not in names_ranks:
    names_ranks[boyname]=rank
   if girlname not in names_ranks:
    names_ranks[girlname]=rank
  sorted_names = sorted(names_ranks.keys())
  for name in sorted_names:
   names.append(name+" "+names_ranks[name])
  return names


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  names = extract_names(sys.argv[1])
  text = '\n'.join(names)

  #If the summary option is given then the names returned by the extract_names function
  #will be written into a seperate files with a '.summary' extension
  if summary :
   try:
    with open(sys.argv[1]+'.summary','w') as outf:#The 'w' in the second argument means write for python
     outf.write(text+'\n')
   except IOError as err:
    print 'Failed to created summary file,possible cause : ',str(err)
 
  else:
   print text 
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
