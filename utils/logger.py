import logging

def save_logs():

    logging.basicConfig(
        filename="logs/restaurant.log",
        level=logging.INFO,
        format= " %(asctime)-20s ||"
                " %(name)-20s ||"
                " %(levelname)-10s ||"
                " %(filename)-25s:%(lineno)-4d ||"
                " %(message)s"
    )

save_logs()

logger = logging.getLogger("Restaurant")

