from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


connection_string = ""
container_name = "notify"
blob_name = "notifyblob.txt"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)
blob_client = container_client.get_blob_client(blob_name)


def readFromDB():
    with open("sent_notice.txt", "wb") as data:
        download_stream = blob_client.download_blob()
        data.write(download_stream.readall())

def updateDB():
    with open("sent_notice.txt", "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

def addToDB(filename):
    with open("sent_notice.txt", "a") as data:
        data.write(filename+"\n")