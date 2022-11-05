from linebot.models import *

def Namelist(name):

    if len(name) == 1:
        message = TemplateSendMessage(
            alt_text = "Signed Name List",
            template = ButtonsTemplate(
                title = "Name List",
                text = "Choose person to setting box",
                actions=[
                    MessageAction(
                        label = name[0],
                        text= name[0]
                    )
                ]
            )
        )
        return message
    else:
        message = TemplateSendMessage(
            alt_text = "Signed Name List",
            template = ButtonsTemplate(
                title = "Name List",
                text = "Choose person to setting box",
                actions = [
                    MessageAction(
                        label = name[0],
                        text = name[0]
                    ),
                    MessageAction(
                        label = name[1],
                        text = name[1]
                    )
                ]
            )
        )
        return message

def Carousel_Weekday():
    message = TemplateSendMessage(
        alt_text='Weekdays',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title = "一 ~ 三",
                    text = "choose a day",
                    actions=[
                        MessageAction(
                            label = "週一",
                            text = "1"
                        ),
                        MessageAction(
                            label = "週二",
                            text = "2"
                        ),
                        MessageAction(
                            label = "週三",
                            text = "3"
                        )
                    ]
                ),
                CarouselColumn(
                    title = "四 ~ 六",
                    text = "choose a day",
                    actions=[
                        MessageAction(
                            label = "週四",
                            text = "4"
                        ),
                        MessageAction(
                            label = "週五",
                            text = "5"
                        ),
                        MessageAction(
                            label = "週六",
                            text = "6"
                        )
                    ]
                ),
                CarouselColumn(
                    title = "日",
                    text = "choose a day",
                    actions=[
                        MessageAction(
                            label = "週日",
                            text = "7"
                        ),
                        MessageAction(
                            label = "週日",
                            text = "7"
                        ),
                        MessageAction(
                            label = "週日",
                            text = "7"
                        )
                    ]
                ),
            ]
        )
    )
    return message

def Carousel_Box():
    message = TemplateSendMessage(
        alt_text='Box',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title = "Boxs",
                    text = "choose a Box",
                    actions=[
                        MessageAction(
                            label = "box1",
                            text = "1"
                        ),
                        MessageAction(
                            label = "box2",
                            text = "2"
                        ),
                        MessageAction(
                            label = "box3",
                            text = "3"
                        )
                    ]
                ),
                CarouselColumn(
                    title = "Boxs",
                    text = "choose a box",
                    actions=[
                        MessageAction(
                            label = "box4",
                            text = "4"
                        ),
                        MessageAction(
                            label = "box5",
                            text = "5"
                        ),
                        MessageAction(
                            label = "box6",
                            text = "6"
                        )
                    ]
                )
            ]
        )
    )
    return message

if __name__ == "__main__":

    name = ["jacky"]
    print(Namelist(name))