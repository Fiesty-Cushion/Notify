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
