from bs4 import Beautiful

html =

 """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1>pavan</h1>
    <p>kalan</p>
</body>
</html>
"""
total = BeautifulSoup(html,"html.parse")
print(total)

