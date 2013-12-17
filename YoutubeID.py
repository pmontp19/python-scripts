import workflow
import re

##get url from previous action
url = workflow.get_input()
match = re.search(r"youtube\.com/.*v=([^&]*)", url)
if match:
  action_out = match.group(1)
else:
  action_out = 'error'

#print action_out

workflow.set_output(action_out)
