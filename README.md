# notify

**A handy tool to receive Pulchowk Notices in your discord server.**

Let's be honest, we all have had that one time when we missed some important notice from campus (I have a couple times now) all
because going through campus website everyday to check for notice is a hassle. Well, this project
is aimed at solving that hassle and let it do that part for you.

## Installation
#### File Structure
```
mkdir notify
cd notify
mkdir docs
mkdir images
git clone https://github.com/Fiesty-Cushion/notice-grabr.git
```
#### Execution
Make sure to change the `webhookURL` in webhook.py.
```
pip install -r requirements.txt
python main.py
```

#### Use Docker Image
```
docker build -t notify .
docker run notify
```


## How it works
Pulchowk Notices are published to `https://pcampus.edu.np/{year}/{month}/{day}/`, notify scrapes content from this url and differentiates each notice with the help of it's title. Normally there are two forms of media posted, PDF and JPEGs. If the content has PDF files, we use `pdf2image` package to render each PDF page to JPG and send it via embedding it to the webhook provided. If the content has JPEGs than we simply embed the image source url to the webhook.  

## Hosting it to Azure
If you wish to host this app to azure, [azure-functions](https://azure.microsoft.com/en-us/products/functions) is the best approach. 
1. Create a Container Instance that pulls image from the Docker Hub. (You can build the docker image and push it to your Docker Hub repo)
2. Create a Blob Storage, and provide the `connection_string`, `container_name` and `blob_name` to `database.py`
3. In Visual Studio, create a `C#` project with `azure-function` template, and use the code from this gist.
4. Publish the azure-function to azure cloud and enjoy! 
