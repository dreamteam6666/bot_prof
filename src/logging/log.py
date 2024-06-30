from main import *
from kb import *
from handlers import *

# TODO сделать/доделать/настроить логирование
logging.basicConfig(level=logging.DEBUG, filename="bot.log", filemode="")


logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")



if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())