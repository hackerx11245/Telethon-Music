import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "28369281"))
    API_HASH = os.environ.get("API_HASH", "934d092497756b7ceb668557fbdf33e4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6279595222:AAGke0Qic-H0_SA8hXYkU22lxDGWe_5uMrg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJoBu3ZBf92lHLVcDqjO2dOh4irTOLPKXvSnLUQTmemlI1MxUDzIMR_jB0u-3oWqa3PaRyswdlq8_e7hjgoE6D4rD76b_qHPVk1cANoL_W3UwHJuV5-xG2EXgsnoV-lnoiJWrjzzyR_VOLdjRKkfnglBncTCHIzNbJHKLWLzORrcaUAqVHlgKILc1gftC3XIX0HL8PEvOYFddwFSt0CnjA9zdlBvx15WLevumQEV6DVhP4tW3EkmDg4yVLNZNsxpdJTr8GqsGBC1ZvWiagGglF3iKDw8KD7Bl7tHvAEfxuvMQ5AI16fgiNQZSR43uytF4EPrfSn-PTb_Nepxfycfztxqm-E=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MattMurdockMusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6008745780")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
