# Webapp

First you have to download the code zip file than you have to create the virtual environment by using cmd python -m venv venv 
activate the venv by using cmd venv\scripts\activate
install the necessary required libraries and dependencies by using requirements.txt use cmd pip install -r requirements.txt (make sure that your requirement file is place in the same dir)
create your django project by using cmd django-admin startproject webapp afterthat navigate to project name using cmd cd webapp
after that you have to create a app for your project by using cmd python manage.py startapp app after that navigate to vscode using cmd code .
I create two more files in app forms.py for django form and urls.py.
I am using django,numpy,pandas,matplotlib,seaborn.
I am creted three function in views.py file 1.handle_uploaded_file function is used to upload csv file and open the file in binary write mode it is used for both reading and writing the file in binary format.To avoid the memory issues it convert into small chunks check the file seize and save it if file size is 0 than raise error if everything it will return thr file path.
2.analyze_data this function is used to read the csv file analyse the data and generate the summary of the data along with plot firstly read the csv file located at file path using pandas if the is empty or invalid it will raise a error by using exception handling throw the error afterthat retrive the first few row of the dataframe for analysing generate summary statics of the numerical in the data frame calculate the number of missing values in each column and convert into dataframe create the histogarm by using seaborn saving plot into buffer converting the dataframe into html included the base64-encoded return dictionary analysis and plot render by the web tem[plate.
3.upload_file this function is used for that handles file uploads from user processes the uploaded file and return the results of the analysis.
