import bs4
import time
import pandas as pd
scraped_data=[]
def scrape():
    bright_star_table=soup.find("table",attrs={"class","wikitable"})
    table_body=bright_star_table.find("tbody")
    table_rows=table_body.find_all("tr")
    for row in table_rows:
        table_cols=row.find_all("td")
        #print(table_cols)
        temp_list=[]
        for col_data in table_cols:
            #print(col_data.text)
            data=col_data.text.strip()
            #print(data)
            temp_list.append(data)
        scraped_data.append(temp_list)
    stars_data=[]
    for i in range(0,len(scraped_data)):
        names=scraped_data[i][1]
        distance=scraped_data[i][3]
        mass=scraped_data[i][5]
        radius=scraped_data[i][6]
        lumi=scraped_data[i][7]
        required_data=[names,distance,mass,radius,lumi]
        stars_data.append(required_data)
    headers=["Name","Distance","Mass","Radius","Luminosity"]
    star_df_1=pd.DataFrame(stars_data,columns=headers)
    star_df_1.to_csv("scraped_data.csv",index=True,index_label="id")
 
