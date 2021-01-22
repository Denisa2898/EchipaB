import veryfi


##https://hub.veryfi.com/signup/verifydemo/

client_id = "vrfo6aTEzg6cb9NTgcCebnK5Og8xMJdW51J6iRG"
client_secret = "wjrpAz6Xg68REzagJH782Np0dbf4VKMWVGhotB4rRMjCC9suDySvuIpyHhufsz703JWd1SWaAtvTNdS3uYDUMLE1O7KfUeErcB1yBwKiVnfoFEjNNG3i2n6E9Khk1coK"
username = "alexandranoaptes"
api_key = "b7da207ac91fcb7b61c85d0686ee5ce6"
client = veryfi.Client(client_id,client_secret, username, api_key)
root_path_f = "C://Users//alexa//OneDrive//Desktop//ProiectOCR//BD_PSDT//images//"

def procesare(file_name):

    json_result1 = client.process_document(file_name)
    return json_result1
