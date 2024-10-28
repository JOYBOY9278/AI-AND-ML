import pandas as pd

d={ "First_name":["Aryan","Rohan","Riya","Yash","Siddhant"], "Last_name":["Singh","Agarwal","Shah","Bhatia","Khanna"], 
"Type":["Full-Time","Itern","Full-Time","Part-Time","Full-Time"], 
"Dept":["Administration","Technical","Administration","Technical","Management"], 
"OE":[2,3,5,7,6], 
"Salary":[20000,5000,10000,10000,20000] } 
df=pd.DataFrame(d) 
print(df) 
av= df.pivot_table(index=['Dept', 'Type'], values='Salary', aggfunc='mean') 
print("\n Average Salary from each dept:\n", av) 
sm= df.pivot_table(index=['Type'], values='Salary', aggfunc=['sum', 'mean', 'count']) 
sm.columns= ['Total Salary', 'Mean Salary', 'Number of Employees'] 
print("\n Sum and Mean of:\n", sm) 
st= df.pivot_table(values='Salary', index='Type', aggfunc='std') 
print("\n Standard Deviation:\n", st) 

 
