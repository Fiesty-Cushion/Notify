from discord_webhook import DiscordWebhook, DiscordEmbed
import os

webhookURL = "<WEBHOOK_URL>"

def embedWebHook(fileURL, title):
    imgDir = os.fsencode("images")
    docsDir = os.fsencode("docs")

    webhook = DiscordWebhook(url=webhookURL)    

    embed = DiscordEmbed(title="Notice!" ,description=f"**{title}**", color='0xDC143C', url=fileURL)
    embed.set_footer(text="Check official website for more details.", icon_url="https://i.imgur.com/0HOdGQE.jpg")
    embeds = [embed]

    i=0
    for file in os.listdir(imgDir):
        embeds.append(DiscordEmbed(url=fileURL))
        filename = os.fsdecode(file)
        with open(f"images/{filename}", "rb") as f:
            print(filename)
            webhook.add_file(file=f.read(), filename=f'{filename}')
        f.close()
        embeds[i].set_image(url=f'attachment://{filename}')
        webhook.add_embed(embeds[i])
        if i==8:
            break
        i+=1
    
    for file in os.listdir(docsDir):
        filename = os.fsdecode(file)
        with open(f"docs/{filename}", "rb") as f:
            webhook.add_file(file=f.read(), filename=f'{filename}')
        f.close()
    
    response = webhook.execute(remove_files=True)
    return(response.status_code)



def imgWebhook(fileURL, title):
    webhook = DiscordWebhook(url=webhookURL)
    embed = DiscordEmbed(title="Notice!" ,description=f"**{title}**", color='0xDC143C', url=fileURL)
    embed.set_footer(text="Check official website for more details.", icon_url="https://i.imgur.com/0HOdGQE.jpg")
    embed.set_image(url=fileURL)
    webhook.add_embed(embed)

    response = webhook.execute()
    return response.status_code

def textWebhook(fileURL, title):    
    webhook = DiscordWebhook(url=webhookURL)
    embed = DiscordEmbed(title="Notice!" ,description=f"**{title}**", color='0xDC143C', url=fileURL)
    embed.set_footer(text="Check official website for more details.", icon_url="https://i.imgur.com/0HOdGQE.jpg")
    webhook.add_embed(embed)

    response = webhook.execute()
    return response.status_code
    