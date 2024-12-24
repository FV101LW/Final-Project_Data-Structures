# Final-Project_Data-Structures
Final Project for Data Structures.

TEST : To be put in html file.
# Read the Python file content
with open('your_file.py', 'r') as file:
    file_content = file.read()

# Create an HTML file to display the content
html_content = f"""
<html>
<head><title>Python File Display</title></head>
<body>
    <h1>Contents of your Python File:</h1>
    <pre>{file_content}</pre>
</body>
</html>
"""

# Save the generated HTML content to a file
with open('display_file.html', 'w') as html_file:
    html_file.write(html_content)

print("HTML file generated: display_file.html")
