# Learning Objectives
- How to fetch internet resources with the Python package urllib
- How to decode urllib body response
- How to use the Python package requests #requestsiswaysimplerthanurllib
- How to make HTTP GET request
- How to make HTTP POST/PUT/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

## Tasks
0-hbtn_status.py
- A Python script that fetches https://alx-intranet.hbtn.io/status
- used the import package urllib
- No packages imported other than urllib
- The body of the response is displayed like the following example (tabulation before -)
- a with statement is used

1-hbtn_header.py
- A Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
- used the import package urllib
- No packages imported other than urllib and sys
- The value of this variable is different for each request
- a with statement is used

2-post_email.py
- A Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
- The email is sent in the email variable
- used the packages urllib and sys
- only urllib and sys packages are imported
- a with statement is used

3-error_code.py
A Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

- The urllib.error.HTTPError exceptions is managed and print: Error code: followed by the HTTP status code
- used the packages urllib and sys
- imported urllib and sys
- arguments passed to the script (number or type) dont have be checked
- used the with statement

4-hbtn_status.py
- A Python script that fetches https://alx-intranet.hbtn.io/status
- used the package requests
- only packages imported are requests
- The body of the response is display like the following example (tabulation before -)

5-hbtn_header.py
- A Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
- used the packages requests and sys
-  imported packages: requests and sys
- The value of this variable is different for each request

6-post_email.py
- A Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
- The email is sent in the variable email
- packages: requests and sys

7-error_code.py
- A Python script that takes in a URL, sends a request to the URL and displays the body of the response.
- If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
- packages: requests and sys

8-json_api.py
- A Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

- The letter is sent in the variable q
- If no argument is given, set q=""
- If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
- Display Not a valid JSON if the JSON is invalid
- Display No result if the JSON is empty
package: requests and sys

10-my_github.py
- A Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
-  used Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
- The first argument: username
- The second argument: password ( a personal access token as password)
- packages: requests and sys
 
100-github_commits.py 
- A Python script that takes 2 arguments in order to solve this challenge.
- The first argument: the repository name
- The second argument: the owner name
- packages: requests and sys
