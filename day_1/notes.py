# to create virtual environment : python3 -m venv "env name"
# to activate env : source flskenv/bin/activate
# to deactivate env : deactivate
# to see installed packages : pip list
# to install packages : pip install "package name"
# to save installed packages to requirements.txt : pip freeze > requirements.txt
#http://127.0.0.1:5000
# http ka mtlb hai ki ye ek communication protocol hai jo web browsers aur servers ke beech hota hai
# 127.0.0.1 mtlb hai ki ye localhost hai, yani ki aapka apna computer ka IP address hai 
# 5000 mtlb hai ki ye port number hai, yani ki aapka flask app 5000 port par run ho raha hai
# flask run karne ke liye aapko terminal me `flask run` command type karna hoga
# quit krne ke liye aapko terminal me `ctrl+c` press karna hoga
# route hamehsa alg hona chahiye, same route par do function nahi ho sakte
# route should be unique
# route should me readable hona chahiye
# route me special characters nahi hone chahiye, jaise ki @, #, $,
# route hamehsa kuch na kuch return karega, chahe wo string ho, html ho, json ho ya koi aur cheez ho
# http methods - GET, POST, PUT, DELETE
# GET :jab hm sirf dekh rhe hai kuch kr nhi rhe hai toh wo GET method hota hai
# POST: jab hm kuch bhej rhe hai server ko toh wo POST method hota hai
# GET: get means to retrieve data from the server, for example, when you visit a webpage, your browser sends a GET request to the server to fetch the content of that page.
# GET: i want some data from you,u cant give data in get
# POST: post means to send data to the server, for example, when you fill out
# post : i want to send you some data
# core object of flask is : request , response , url_for ,session , redirect ,
# to run another flask app using same env use : flask --app app1 run
# return reder_template("file name") is used to render html file and join the file 
# ------------------------------------------------------------------------------------

# jinja 2 
# ye ek templating engine hai jo flask me use hota hai
# jinja2 ka use karke hum dynamic html pages create kar sakte hai
# jinja2 me hum python code ko html me embed kar sakte hai
# jinja2 me hum variables, loops, conditionals etc use kar sakte hai
# jinja2 me hum {{ }} ka use karke variables ko access kar sakte hai
# jinja2 me hum {% %} ka use karke loops aur conditionals ko access