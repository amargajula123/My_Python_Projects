from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq # uReq is the alias or object / variable of urlopen
import pandas as pd

import sys
from exception import ReviewException

# NOTE : for this project use ver_env is "ReviewFlask_env_3"

app = Flask(__name__)

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")   #  render = ఇవ్వడం / అందించు

@app.route('/review',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","")
            print(f"searchString = {searchString}")
            print("request.form['content'] = ",request.form['content'])
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = uReq(flipkart_url) # we are pinging the url here
            flipkartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "cPHDOP col-12-12"})
            if len(bigboxes) > 3:
                del bigboxes[0:3]
            else:
                raise ReviewException("Not enough product boxes found",sys)
            # del bigboxes[0:3]  # why deleting frant 3 infor means there we wont find and "href"

            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodRes = requests.get(productLink)
            prodRes.encoding='utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            print(prod_html)
            commentboxes = prod_html.find_all('div', {'class': "RcXBOT"})

            # filename = searchString + ".csv"
            # fw = open(filename, "w")
            # headers = "Product, Customer Name, Rating, Heading, Comment \n"
            # fw.write(headers)
            reviews = []
            for commentbox in commentboxes:
                try:
                    if commentbox and hasattr(commentbox, 'div') and hasattr(commentbox.div, 'div'):
                        name_tag = commentbox.div.div.find('p', {'class': "_2NsDsF AwS1CA"})
                        name = name_tag.text if name_tag else "No Name"
                        if not name_tag:
                            raise ReviewException("Name tag not found", sys)
                    else:
                        name = "No Name"
                        raise ReviewException("div structure not found in commentbox", sys)
                except Exception as e:
                    name = "No Name"
                    raise ReviewException(e, sys) from e

                try:
                    rating_tag = commentbox.div.div.div.div
                    rating = rating_tag.text if rating_tag else "No Rating"
                    if not rating_tag:
                        raise ReviewException("Rating tag not found", sys)
                except Exception as e:
                    rating = "No Rating"
                    raise ReviewException(e, sys) from e

                try:
                    comment_head_tag = commentbox.div.div.div.p
                    commentHead = comment_head_tag.text if comment_head_tag else "No Comment Heading"
                    if not comment_head_tag:
                        raise ReviewException("Comment heading tag not found", sys)
                except Exception as e:
                    commentHead = "No Comment Heading"
                    raise ReviewException(e, sys) from e

                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    custComment = comtag[0].div.text if comtag and comtag[0].div else "No Comment"
                    if not comtag or not comtag[0].div:
                        raise ReviewException("Comment text not found", sys)
                except Exception as e:
                    custComment = "No Comment"
                    raise ReviewException(e, sys) from e

                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                          "Comment": custComment}
                reviews.append(mydict)

            df = pd.DataFrame(reviews)
            df.to_csv(f"{searchString}" + ".csv", index=False)

            return render_template('results.html', reviews=reviews[0:(len(reviews)-1)])
        except Exception as e:
            # print('The Exception message is: ',e)
            raise ReviewException(e, sys) from e
            # return 'something is wrong'


    # return render_template('results.html')

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
    # port = int(os.environ.get("PORT", 5000))  # Get port from Heroku, default to 5000 locally
    # app.run(host="0.0.0.0", port=port, debug=True)




    # TASK try to take search string from postman and try to load that entire data into pandas,sql,mongoDB

    # x = None
    # hasattr(x, 'div')  # False
    #
    # from bs4 import BeautifulSoup
    #
    # html = "<div><p>Hello</p></div>"
    # soup = BeautifulSoup(html, "html.parser")
    # tag = soup.find('div')
    #
    # hasattr(tag, 'text')  # True
    # hasattr(tag, 'div')  # True (since tag.div exists)
